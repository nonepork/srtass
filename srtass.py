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

for filename in files:
    shift_timecode(filename, seconds, milliseconds, minutes)
