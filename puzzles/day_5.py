from rich.progress import track

from utils import read_input


def check_id(id: int, ranges: list[tuple[int, int]]) -> bool:
    for r in ranges:
        min, max = r
        if id >= min and id <= max:
            return True

    return False


def pt_1(input_path: str) -> int:
    lines = read_input(input_path)
    fresh_ranges: list[tuple[int, int]] = []  # ranges are inclusive
    ingredient_ids: list[int] = []

    fresh_ids: list[int] = []

    is_ranges = True
    for line in lines:
        if len(line) == 0:
            is_ranges = False
            continue

        if is_ranges:
            fresh_range = line.split("-")

            fresh_ranges.append((int(fresh_range[0]), int(fresh_range[1])))

        else:
            ingredient_ids.append(int(line))

    for i in track(ingredient_ids, description="Processing ids..."):
        if check_id(i, fresh_ranges):
            fresh_ids.append(i)

    return len(fresh_ids)


def pt_2(input_path: str) -> int:
    lines = read_input(input_path)
    fresh_ranges: list[tuple[int, int]] = []  # ranges are inclusive

    is_ranges = True
    for line in lines:
        if len(line) == 0:
            is_ranges = False
            continue

        if is_ranges:
            fresh_range = line.split("-")

            fresh_ranges.append((int(fresh_range[0]), int(fresh_range[1])))

        else:
            continue

    fresh_ranges.sort(key=lambda x: x[0])

    new_ranges: set[tuple[int, int]] = set()  # ranges are inclusive
    remove_ranges: list[tuple[int, int]] = []  # ranges are inclusive
    checked_ranges: list[tuple[int, int]] = []  # ranges are inclusive

    print("original")
    for i in fresh_ranges:
        print(i)

    print("num ranges", len(fresh_ranges))

    for i in fresh_ranges:
        # print("checking", i)
        if i in remove_ranges:
            # print("in remove", remove_ranges)
            continue

        i_min, i_max = i
        for j in fresh_ranges:
            if j in checked_ranges or j in remove_ranges:
                continue

            # print("checking against", j)
            j_min, j_max = j
            if i_min == j_min or i_max >= j_min or i_max + 1 == j_min or i_max == j_max:
                if j_max > i_max:
                    i_max = j_max
                remove_ranges.append(j)

        checked_ranges.append(i)
        new_ranges.add((i_min, i_max))

    print("new", len(new_ranges))

    ranges = sorted(new_ranges, key=lambda x: x[0])

    total = 0
    for i in ranges:
        min, max = i

        if max == min:
            continue

        diff = max - min
        total += max - min + 1
        print(f"{i} \t {diff}")

    return total


# 371289297497547 too high
# 352478980357921 too high
# 352478980357908
# 352478980357916
# 345755049374932 RIGHT ANSWER
