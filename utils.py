from pathlib import Path


def read_input(input: str | Path):
    with open(input) as file:
        lines = file.readlines()
        stripped = [" ".join(line.split()) for line in lines]
        return stripped
