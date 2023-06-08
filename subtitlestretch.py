import re
from datetime import datetime, timedelta

file_path = './Operation Scorpio 蝎子战士 1992.srt'
target_path = "./Operation Scorpio 蝎子战士 1992 Modified.srt"
ratio_diff = 1.04158888501
second_offset = 24.08799442

def convertToSeconds(timestamp):
    # Convert the timestamp to a datetime object
    dt = datetime.strptime(timestamp, "%H:%M:%S,%f")
    # Calculate the total seconds
    total_seconds = timedelta(hours=dt.hour, minutes=dt.minute, seconds=dt.second, microseconds=dt.microsecond).total_seconds()
    return total_seconds



def convertToStringTimestamp(seconds):
    # Create a timedelta object using the seconds
    delta = timedelta(seconds=seconds)

    # Format the timedelta as a timestamp string
    timestamp = str(delta)

    # Split the timestamp into hours, minutes, seconds, and microseconds
    hours, remainder = divmod(delta.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    seconds, microseconds = divmod(seconds, 1)

    # Format the hours, minutes, and seconds with leading zeros
    time_str = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d},{int(microseconds * 1000):03d}"

    return time_str

def convertSpecificTime(timeStr):
    seconds = (convertToSeconds(timeStr) * ratio_diff) + second_offset
    return convertToStringTimestamp(seconds)

def convertTimingToNewRatio(line):
    if line.startswith("00:") or line.startswith("01:"):
        times = line.split(" --> ")
        secondArr = map(convertSpecificTime, times)
        return " --> ".join(secondArr)
    else:
        return line

def changeTimingOfSub():
    with open(file_path, "r") as file:
        file_content = file.read()
    
    file_lines = file_content.split("\n")
    converted_lines = map(convertTimingToNewRatio, file_lines)
    new_file_content = "\n".join(converted_lines)

    with open(target_path, 'w') as file:
        file.write(new_file_content)


    # pattern = r'^(?:00:|01:).*?\n\n'
    # pattern = r'^(?:00:|01:).*?\n'
    # matches = re.findall(pattern, file_content, re.MULTILINE)
    # print(matches)
    # for match in matches:
    #     matchSplit = match.split("\n")        
    #     timing = matchSplit[0].split(" --> ")
    #     time_start = convertToSeconds(timing[0]) * ratio_diff
    #     time_end = convertToSeconds(timing[0])
    #     sub = "\n".join(matchSplit[1:])
    #     obj = {
    #         "time_start": convertToSeconds(timing[0]),
    #         "time_end": convertToSeconds(timing[1]),
    #         "sub": sub.strip(),
    #     }
    #     objectArr.append(obj)
    

changeTimingOfSub()


# ORIGINAL START: 00:00:55,640
# 55.64
# ORIGINAL END: 01:34:25,360
# 5665.36

# 5609.72


# MODIFIED START: 00:01:22,042
# 82.042
# MODIFIED END: 01:38:45,064
# 5925.064

# 5843.022

# Ratio_diff = 1.04158888501

# 57.954005562
# 5900.97600558

# SECOND DIFF = 24.087994438
# SECOND DIFF = 24.08799442

# str1 = "00:00:55,640"
# str2 = "01:34:25,360"

# str3 = "00:01:22,042"
# str4 = "01:38:45,064"