from time import sleep

from utils import read_input


def check_roll(spots: list[tuple[int, int]], diagram: list[list[str]]) -> bool:
    rolls = 0

    for coords in spots:
        row, col = coords
        if diagram[row][col] == "@" or diagram[row][col] == "x":
            rolls += 1

    return rolls < 4


def remove_rolls(diagram: list[list[str]]) -> None:
    for row in range(len(diagram)):
        for col in range(len(diagram[0])):
            if diagram[row][col] == "x":
                diagram[row][col] = "."


def show_diagram(diagram: list[list[str]]) -> None:
    for row in range(len(diagram)):
        print("".join(diagram[row]))


def check_accessible(coords: tuple[int, int], diagram: list[list[str]]) -> bool:
    rows_n = len(diagram) - 1
    cols_n = len(diagram[0]) - 1

    match coords:
        case (0, col):  # first row
            if col == 0 or col == cols_n:
                return True

            spots = [(0, col - 1), (0, col + 1), (1, col - 1), (1, col), (1, col + 1)]
            return check_roll(spots, diagram)

        case (row, col) if row == rows_n:  # last row
            if col == 0 or col == cols_n:
                return True

            spots = [
                (row, col - 1),
                (row, col + 1),
                (row - 1, col - 1),
                (row - 1, col),
                (row - 1, col + 1),
            ]
            return check_roll(spots, diagram)

        case (row, 0):  # first col
            spots = [
                (row - 1, col),
                (row + 1, col),
                (row - 1, col + 1),
                (row, col + 1),
                (row + 1, col + 1),
            ]
            return check_roll(spots, diagram)

        case (row, col) if col == cols_n:  # last col
            spots = [
                (row - 1, col),
                (row + 1, col),
                (row - 1, col - 1),
                (row, col - 1),
                (row + 1, col - 1),
            ]
            return check_roll(spots, diagram)

        case (row, col):
            spots = [
                (row - 1, col - 1),
                (row - 1, col),
                (row - 1, col + 1),
                (row, col - 1),
                (row, col + 1),
                (row + 1, col - 1),
                (row + 1, col),
                (row + 1, col + 1),
            ]
            return check_roll(spots, diagram)


def pt_1(input_path: str) -> int:
    lines = read_input(input_path)
    diagram: list[list[str]] = []

    accessible_n: int = 0

    for line in lines:
        row: list[str] = []
        for i in line:
            row.append(i)
        diagram.append(row)

    for row in range(len(diagram)):
        for col in range(len(diagram[0])):
            if diagram[row][col] != "@" and diagram[row][col] != "x":
                continue
            if check_accessible((row, col), diagram):
                accessible_n += 1

    return accessible_n


def pt_2(input_path: str) -> int:
    lines = read_input(input_path)
    diagram: list[list[str]] = []

    accessible_n: int = 1

    for line in lines:
        row: list[str] = []
        for i in line:
            row.append(i)
        diagram.append(row)

    round_counts: list[int] = []

    rounds = 1

    while accessible_n > 0:
        accessible_n = 0
        print(f"Checking rolls {rounds}")
        show_diagram(diagram)
        for row in range(len(diagram)):
            for col in range(len(diagram[0])):
                if diagram[row][col] != "@" and diagram[row][col] != "x":
                    continue
                if check_accessible((row, col), diagram):
                    accessible_n += 1
                    diagram[row][col] = "x"

        print(f"Removing {accessible_n} rolls")

        remove_rolls(diagram)
        round_counts.append(accessible_n)
        print(round_counts)
        rounds += 1
        sleep(0.25)

    return sum(round_counts)
