# Subtitle Stretcher
This is a Python script using Python 3.11.1 that I wrote that simply takes a seconds offset and a ratio to change the speed at which subtitles in SRT files play to the time that was given. 

## THE PROBLEM
In certain old films that I would watch, there was an issue where the subtitles would play at a different speed than the video. It wouldn't matter how often you would delay the subtitles, the subtitles would eventually become too slow or go too fast for it to reasonably work.

## THE SOLUTION
Rather than manually add the times, I thought it would be better to instead write a script that adjusts the times by the approximate amount. I wrote a Python script that looks for timestamps on a line and adjusts them based off a given ratio and seconds offset. These times are calculated via taking the time of where the very first sub should play and the time where the very last sub should play in the modified video you are watching. Given that the only difference in the video that the original SRT file is that the video plays at a different speed, we can calculate the seconds offset and the speed difference to adjust the subs using these formulas:

OLD TIME RUN = OLD END TIME - OLD START TIME

NEW TIME RUN = NEW END TIME - NEW START TIME

SPEED RATIO = NEW TIME RUN / OLD TIME RUN

SECONDS OFFSET = NEW TIME RUN - (OLD TIME RUN * SPEED RATIO) 

With seconds offset & speed difference we can then apply these numbers against the subtitle times:
time * SPEED RATIO + SECONDS OFFSET

And this should generally move the sub to the right spot.


## TODO:
Right now a lot of these numbers are hard coded, the hope is to next include an option to choose the file that we're looking at and have a prompt that asks for the new start and new end times to calculate the numbers needed. Once that's completed the next piece would be to get this to work with other subtitle files such as .ASS and .SSA files.
