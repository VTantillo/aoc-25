import math


def get_input(path: str) -> list[str]:
    with open(path) as file:
        lines = file.readlines()
        stripped = [val for line in lines for val in line.split(",")]
        return stripped


def pt_1(input_path: str):
    lines = get_input(input_path)
    nums: list[int] = []

    for line in lines:
        [a, b] = line.split("-")

        for x in range(int(a), int(b) + 1):
            x_str = str(x)

            if len(x_str) % 2 != 0:
                continue

            half = math.floor(len(x_str) / 2)
            a_str = x_str[:half]
            b_str = x_str[half:]

            if a_str == b_str:
                nums.append(x)

    print(sum(nums))


def pt_2(input_path: str):
    lines = get_input(input_path)
    nums: set[int] = set()

    for line in lines:
        print(line)
        [a, b] = line.split("-")

        for x in range(int(a), int(b) + 1):
            x_str = str(x)

            l_strs: list[str] = []

            for length in range(1, math.floor(len(x_str) / 2) + 1):
                l_strs = [x_str[i : i + length] for i in range(0, len(x_str), length)]

                first = l_strs[0]
                if all(i == first for i in l_strs):
                    nums.add(x)

        print("num of nums", len(nums))

    print(nums)
    print("sum", sum(nums))


# 79244580806 is too hight
