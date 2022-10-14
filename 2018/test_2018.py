from A_01.solution import sum_all, find_repeted_value
from B_02.solution import check_frequency, compare_strings
from C_03.solution import find_overlap, id_without_overlap
from D_04.solution import repose_record
from E_05.solution import alchemical_reductuion, alchemical_reductuion_2
from F_06.solution import ChronalCoordinates, ChronalCoordinates_2
from G_07.solution import InstructionSteps
from H_08.solution import memory_maneuver
from I_09.solution import marble_mania

from N_14.solution import chocolate_charts, chocolate_charts_backward

from P_16.solution import (
    addition_immediate,
    addition_registry,
    multiplication_immediate,
    multiplication_registry,
    assigment_register,
    assigment_immediate,
)
from R_18.solution import settlers_of_north_pole


def test_A_1():
    assert sum_all([1, -2, 3, 1]) == 3
    assert sum_all([1, 1, 1]) == 3
    assert sum_all([1, 1, -2]) == 0
    assert sum_all([-1, -2, -3]) == -6


def test_A_2():
    assert find_repeted_value([1, -2, 3, 1]) == 2
    assert find_repeted_value([1, -1]) == 0
    assert find_repeted_value([3, 3, 4, -2, -4]) == 10
    assert find_repeted_value([-6, 3, 8, 5, -6]) == 5
    assert find_repeted_value([7, 7, -2, -7, -4]) == 14


def test_B_1():
    assert check_frequency('abcdef') == (0, 0)
    assert check_frequency('bababc') == (1, 1)
    assert check_frequency('abbcde') == (1, 0)
    assert check_frequency('abcccd') == (0, 1)
    assert check_frequency('aabcdd') == (1, 0)
    assert check_frequency('abcdee') == (1, 0)
    assert check_frequency('ababab') == (0, 1)


def test_B_2():
    data = [
        'abcde',
        'fghij',
        'klmno',
        'pqrst',
        'fguij',
        'axcye',
        'wvxyz'
    ]
    assert compare_strings(data) == 'fgij'


def test_C_1():
    data = [
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2',
    ]
    assert find_overlap(data) == 4


def test_C_2():
    data = [
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2',
    ]
    assert id_without_overlap(data) == 3


def test_D():
    data = [
        '[1518-11-01 00:00] Guard #10 begins shift',
        '[1518-11-01 00:05] falls asleep',
        '[1518-11-01 00:25] wakes up',
        '[1518-11-01 00:30] falls asleep',
        '[1518-11-01 00:55] wakes up',
        '[1518-11-01 23:58] Guard #99 begins shift',
        '[1518-11-02 00:40] falls asleep',
        '[1518-11-02 00:50] wakes up',
        '[1518-11-03 00:05] Guard #10 begins shift',
        '[1518-11-03 00:24] falls asleep',
        '[1518-11-03 00:29] wakes up',
        '[1518-11-04 00:02] Guard #99 begins shift',
        '[1518-11-04 00:36] falls asleep',
        '[1518-11-04 00:46] wakes up',
        '[1518-11-05 00:03] Guard #99 begins shift',
        '[1518-11-05 00:45] falls asleep',
        '[1518-11-05 00:55] wakes up',
    ]
    assert repose_record(data) == (240, 4455)


def test_E_1():
    data = 'dabAcCaCBAcCcaDA'
    assert alchemical_reductuion(data) == 10


def test_E_2():
    data = 'dabAcCaCBAcCcaDA'
    assert alchemical_reductuion_2(data) == 4


def test_F_1():
    data = [
        [1, 1],
        [1, 6],
        [8, 3],
        [3, 4],
        [5, 5],
        [8, 9]
    ]
    assert ChronalCoordinates(data) == 17


def test_F_2():
    data = [
        [1, 1],
        [1, 6],
        [8, 3],
        [3, 4],
        [5, 5],
        [8, 9]
    ]
    assert ChronalCoordinates_2(data, 32) == 16


def test_G_1():
    data = [
        'Step C must be finished before step A can begin.',
        'Step C must be finished before step F can begin.',
        'Step A must be finished before step B can begin.',
        'Step A must be finished before step D can begin.',
        'Step B must be finished before step E can begin.',
        'Step D must be finished before step E can begin.',
        'Step F must be finished before step E can begin.',
    ]
    assert InstructionSteps(data) == 'CABDFE'


def test_H():
    data = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
    assert memory_maneuver(data) == (138, 66)


def test_I():
    assert marble_mania(10, 1618) == 8317
    assert marble_mania(13, 7999) == 146373
    assert marble_mania(21, 6111) == 54718
    assert marble_mania(30, 5807) == 37305


def test_N_1():
    assert chocolate_charts(9) == '5158916779'
    assert chocolate_charts(5) == '0124515891'
    assert chocolate_charts(18) == '9251071085'
    assert chocolate_charts(2018) == '5941429882'


def test_N_2():
    assert chocolate_charts_backward('51589') == 9
    assert chocolate_charts_backward('01245') == 5
    assert chocolate_charts_backward('92510') == 18
    assert chocolate_charts_backward('59414') == 2018


def test_P():
    before_data = [3, 2, 1, 1]
    after_data = [3, 2, 2, 1]
    A = 2
    B = 1
    C = 2
    assert addition_immediate([3, 2, 1, 1], [3, 2, 2, 1], 2, 1, 2)

    before_data = [3, 2, 1, 1]
    after_data = [3, 2, 3, 1]
    A = 2
    B = 1
    C = 2
    assert addition_registry(before_data, after_data, A, B, C)

    before_data = [3, 2, 1, 1]
    after_data = [3, 2, 1, 1]
    A = 2
    B = 1
    C = 2
    assert multiplication_immediate(before_data, after_data, A, B, C)

    before_data = [3, 2, 1, 1]
    after_data = [3, 2, 2, 1]
    A = 2
    B = 1
    C = 2
    assert multiplication_registry(before_data, after_data, A, B, C)

    before_data = [3, 2, 1, 1]
    after_data = [3, 2, 2, 1]
    A = 2
    B = 1
    C = 2
    assert assigment_immediate(before_data, after_data, A, B, C)

    before_data = [3, 2, 1, 1]
    after_data = [3, 2, 1, 1]
    A = 2
    B = 1
    C = 2
    assert assigment_register(before_data, after_data, A, B, C)


def test_R():
    data = [
        ['.', '#', '.', '#', '.', '.', '.', '|', '#', '.'],
        ['.', '.', '.', '.', '.', '#', '|', '#', '#', '|'],
        ['.', '|', '.', '.', '|', '.', '.', '.', '#', '.'],
        ['.', '.', '|', '#', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '#', '|', '|', '|', '#', '|', '#', '|'],
        ['.', '.', '.', '#', '.', '|', '|', '.', '.', '.'],
        ['.', '|', '.', '.', '.', '.', '|', '.', '.', '.'],
        ['|', '|', '.', '.', '.', '#', '|', '.', '#', '|'],
        ['|', '.', '|', '|', '|', '|', '.', '.', '|', '.'],
        ['.', '.', '.', '#', '.', '|', '.', '.', '|', '.'],
    ]
    assert settlers_of_north_pole(data) == 1147
