import re
from tools.subtime import SubTime


def shift_timecode(file, seconds=0, milliseconds=0, minutes=0):
    new_filename = ""

    with open(file, encoding="utf-8") as o_f:
        old_file = o_f.readlines()
        if file.endswith(".srt"):
            timecode = re.compile(
                r"\-?\d*\d:\d\d:\d\d,\d{3}\s\-\-\>\s\-?\d*\d:\d\d:\d\d,\d{3}"
            )
            for index, line in enumerate(old_file):
                match_line = timecode.match(line)
                if match_line:
                    line = re.split(":|,| |\n", line)
                    time_line = SubTime(seconds, milliseconds, minutes)
                    first_timecode = time_line.timechanger(line, 3)
                    next_timecode = time_line.timechanger(first_timecode, 8)
                    old_file[index] = (
                        f"{line[0]}:{line[1]}:{line[2]},{line[3]} {line[4]} "
                        + f"{line[5]}:{line[6]}:{line[7]},{line[8]}\n"
                    )

            new_filename = file[:-3] + "matched" + ".srt"

        elif file.endswith(".ass"):
            for index, line in enumerate(old_file):
                if line.startswith("Dialogue:"):
                    line = re.split("[:,.]", line, maxsplit=10)
                    # .ass files have two-digit number milliseconds
                    # so i do them 3-digit and 2 digit again later
                    # TODO: this is wrong, fix this
                    line[5] = line[5] + "0"
                    line[9] = line[9] + "0"
                    time_line = SubTime(seconds, milliseconds, minutes)
                    first_timecode = time_line.timechanger(line, 5)
                    next_timecode = time_line.timechanger(first_timecode, 9)
                    # Don't know is this necessary or not.
                    line[5] = line[5][:-1]
                    line[9] = line[9][:-1]
                    old_file[index] = "%s:%s,%s:%s:%s.%s,%s:%s:%s.%s,%s" % (
                        line[0],
                        line[1],
                        line[2],
                        line[3],
                        line[4],
                        line[5],
                        line[6],
                        line[7],
                        line[8],
                        line[9],
                        line[10],
                    )

            new_filename = file[:-3] + "matched" + ".ass"
    with open(new_filename, "w", encoding="utf-8") as new_file:
        for line in old_file:
            new_file.write(line)
