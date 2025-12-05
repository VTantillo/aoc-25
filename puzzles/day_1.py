import math
from pathlib import Path

from utils import read_input

min = 0
max = 99


def pt_2(input_path: Path | str):
    lines = read_input(input_path)

    zeros = 0

    current = 50

    input_line = 1

    for line in lines:
        clicks = int(line[1:])
        before = current

        match line[0]:
            case "R":
                total = current + clicks
                current = total % 100
            case "L":
                total = current - clicks
                current = total % 100
            case _:
                raise ValueError("Should never be here")

        passes = math.floor(abs(total) / 100)

        if total == 0 or (total < 0 and before != 0):
            passes += 1

        zeros += passes

        print(
            f"{input_line}: \t {before} \t {line} \t {total} \t {current} \t {passes} \t {zeros}"
        )
        input_line += 1

    print(zeros)
    print("huh")
