from utils import read_input


def find_joltage(bank: str, slots_n: int = 12) -> int:
    slots: list[str] = []

    start_pos = 0
    end_pos = len(bank) - (slots_n - 1)

    slot_max = 9
    cur_len = len(slots)
    while len(slots) != slots_n or slot_max < 0:
        print(f"Found {len(slots)} ]t Start {start_pos} \t End {end_pos}")
        for i in range(start_pos, end_pos):
            if int(bank[i]) == slot_max:
                slots.append(bank[i])
                start_pos = i + 1
                break

        if cur_len == len(slots):
            slot_max -= 1
            continue

        cur_len = len(slots)
        slot_max = 9
        end_pos += 1

    if slot_max < 0:
        print("THERE WAS AN ERROR HALP")

    joltage = "".join(slots)

    return int(joltage)


def pt_1(input_path: str) -> int:
    banks = read_input(input_path)

    joltages: list[int] = []

    for bank in banks:
        joltages.append(find_joltage(bank))

    print(sum(joltages))

    return sum(joltages)


def pt_2():
    pass


if __name__ == "__main__":
    pt_1()
