import pytest

from puzzles.day_3 import find_joltage, pt_1


@pytest.mark.parametrize(
    "input,expected",
    [
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
    ],
)
def test_find_joltage(input, expected):
    assert find_joltage(input) == expected


def test_pt_1():
    total_joltage = pt_1()
    assert total_joltage == 357
