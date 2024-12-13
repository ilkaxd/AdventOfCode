from day_01.solution import (
    find_distance as solution_01_A,
    find_similarity as solution_01_B
)
from day_02.solution import count_safe as solution_02
from day_03.solution import find_muls as solution_03
from day_04.solution import (
    find_word as solution_04_A,
    find_word_2 as solution_04_B
)


def test_01():
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]
    assert solution_01_A(left_list, right_list) == 11
    assert solution_01_B(left_list, right_list) == 31


def test_02():
    data = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert solution_02(data) == 2
    assert solution_02(data, True) == 4


def test_03():
    data = (
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)"
        "+mul(32,64]then(mul(11,8)mul(8,5))"
    )
    assert solution_03(data) == 161

    data = (
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)"
        "+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
    assert solution_03(data, True) == 48


def test_04():
    data = [
        ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M",],
        ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A",],
        ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M",],
        ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X",],
        ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M",],
        ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A",],
        ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S",],
        ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A",],
        ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M",],
        ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X",],
    ]
    assert solution_04_A(data) == 18
    assert solution_04_B(data) == 9
