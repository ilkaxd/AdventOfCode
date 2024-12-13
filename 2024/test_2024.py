from day_01.solution import (
    find_distance as solution_01_A,
    find_similarity as solution_01_B
)
from day_02.solution import count_safe as solution_02


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
