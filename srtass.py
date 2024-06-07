import os
import argparse
from tools.timecodes import shift_timecode

parser = argparse.ArgumentParser(
    description="""Shift subtitle timecodes.
    Supported formats: .ass and .srt""")

parser.add_argument(
    'filenames', nargs='+', help="""Path to the subtitle file that needs to be changed.""")

parser.add_argument(
    '-s', '--seconds', type=int, default=0,
    help="""The seconds for which the timecode needs to be corrected.
    Like: 2 or -12.""")

parser.add_argument(
    '-ml', '--milliseconds', type=int, default=0,
    help="""The milliseconds for which the timecode needs to be corrected.""")

parser.add_argument(
    '-min', '--minutes', type=int, default=0,
    help="""The minutes for which the timecode needs to be corrected.""")

args = parser.parse_args()
files = args.filenames
seconds = args.seconds
milliseconds = args.milliseconds
minutes = args.minutes

# TODO: centralized your file check mechanism
for filename in files:
    if os.path.isdir(filename):
        for deeper_file in os.listdir(filename):
            deeper_file = os.path.join(filename, deeper_file)
            shift_timecode(deeper_file, seconds, milliseconds, minutes)
    elif os.path.isfile(filename):
        shift_timecode(filename, seconds, milliseconds, minutes)
    else:
        raise Exception("What did you just feed me?")
