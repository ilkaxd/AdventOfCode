from A_01.solution import find_floor, find_position
from B_02.solution import find_square, find_ribbon_length
from C_03.solution import find_unique_houses, find_unique_houses_2
from D_04.solution import findMinimumHash
from E_05.solution import IsNice, IsNice_2
from F_06.solution import First, Second
from G_07.solution import BitwiseOperations
from H_08.solution import CountSimbols, CountRawSimbols
from I_09.solution import FindTargetDistance
from J_10.solution import look_and_say
from K_11.solution import is_valid_password, find_new_password
from L_12.solution import count_values, count_values_2
from M_13.solution import first, second
from N_14.solution import reindeer_olympics, reindeer_olympics_2
from O_15.solution import best_combination
from P_16.solution import analize_sue, find_sue
from Q_17.solution import fill_refregirator, min_needed
from R_18.solution import swap_light
from S_19.solution import medicine_for_Rudolpf, medicine_for_Rudolpf_2
from T_20.solution import infinite_elves_and_infinite_houses
from U_21.solution import Player
# from V_22.solution 
from W_23.solution import use_register
# from X_24.solution import 
from Y_25.solution import build_graph


def test_A_1():
    assert find_floor('(())') == 0
    assert find_floor('()()') == 0
    assert find_floor('(((') == 3
    assert find_floor('(()(()(') == 3
    assert find_floor('))(((((') == 3
    assert find_floor('())') == -1
    assert find_floor('))(') == -1
    assert find_floor(')))') == -3
    assert find_floor(')())())') == -3


def test_A_2():
    assert find_position(')') == 1
    assert find_position('()())') == 5


def test_B_1():
    assert find_square('2x3x4') == 58
    assert find_square('1x1x10') == 43


def test_B_2():
    assert find_ribbon_length('2x3x4') == 34


def test_C_1():
    assert find_unique_houses('>') == 2
    assert find_unique_houses('^>v<') == 4
    assert find_unique_houses('^v^v^v^v^v') == 2


def test_C_2():
    assert find_unique_houses_2('^v') == 3
    assert find_unique_houses_2('^>v<') == 3
    assert find_unique_houses_2('^v^v^v^v^v') == 11


def test_D():
    assert findMinimumHash('abcdef', 5) == 609043
    assert findMinimumHash('pqrstuv', 5) == 1048970


def test_E_1():
    assert IsNice('ugknbfddgicrmopn') is True
    assert IsNice('aaa') is True
    assert IsNice('jchzalrnumimnmhp') is False
    assert IsNice('haegwjzuvuyypxyu') is False
    assert IsNice('dvszwmarrgswjxmb') is False


def test_E_2():
    assert IsNice_2('qjhvhtzxzqqjkmpb') is True
    assert IsNice_2('xxyxx') is True
    assert IsNice_2('xyxy') is True
    assert IsNice_2('aabadafgaa') is True

    assert IsNice_2('uurcxstgmygtbstg') is False
    assert IsNice_2('ieodomkazucvgmuy') is False
    assert IsNice_2('qrqitdvyoneqyxcg') is False
    assert IsNice_2('aaa') is False


def test_F_1():
    assert First(['turn on 0,0 through 999,999']) == 1_000_000
    assert First(['toggle 0,0 through 999,0']) == 1_000
    assert First(['turn off 499,499 through 500,500']) == 0


def test_F_2():
    assert Second(['turn on 0,0 through 0,0']) == 1
    assert Second(['toggle 0,0 through 999,999']) == 2_000_000


def test_G():
    operations = [
        '123 -> x',
        '456 -> y',
        'x AND y -> d',
        'x OR y -> e',
        'x LSHIFT 2 -> f',
        'y RSHIFT 2 -> g',
        'NOT x -> h',
        'NOT y -> i'
    ]
    result = BitwiseOperations(operations)
    assert result['d'] == 72
    assert result['e'] == 507
    assert result['f'] == 492
    assert result['g'] == 114
    assert result['h'] == 65412
    assert result['i'] == 65079
    assert result['x'] == 123
    assert result['y'] == 456


def test_H_1():
    rows = [
        r'""',
        r'"abc"',
        r'"aaa\"aaa"',
        r'"\x27"'
    ]
    assert CountSimbols(rows) == 12


def test_H_2():
    rows = [
        r'""',
        r'"abc"',
        r'"aaa\"aaa"',
        r'"\x27"'
    ]
    assert CountRawSimbols(rows) == 19


def test_I():
    data = [
        'London to Dublin = 464',
        'London to Belfast = 518',
        'Dublin to Belfast = 141'
    ]
    assert FindTargetDistance(data) == 605
    assert FindTargetDistance(data, min_find=False) == 982


def test_J():
    assert look_and_say('1') == '11'
    assert look_and_say('11') == '21'
    assert look_and_say('21') == '1211'
    assert look_and_say('1211') == '111221'
    assert look_and_say('111221') == '312211'


def test_K():
    assert not is_valid_password('hijklmmn')
    assert not is_valid_password('abbceffg')
    assert not is_valid_password('abbcegjk')
    assert find_new_password('abcdefgh') == 'abcdffaa'
    assert find_new_password('ghijklmn') == 'ghjaabcc'


def test_L_1():
    assert count_values([1, 2, 3]) == 6
    assert count_values({'a': 2, 'b': 4}) == 6
    assert count_values([[[3]]]) == 3
    assert count_values({'a': [-1, 1]}) == 0
    assert count_values([-1, {'a': 1}]) == 0
    assert count_values([]) == 0
    assert count_values({}) == 0


def test_L_2():
    assert count_values_2([1, 2, 3]) == 6
    assert count_values_2([1, {'c': 'red', 'b': 2}, 3]) == 4
    assert count_values_2({'d': 'red', 'e': [1, 2, 3, 4], 'f': 5}) == 0
    assert count_values_2([1, 'red', 5]) == 6


def test_M_1():
    data = [
        'Alice would gain 54 happiness units by sitting next to Bob.',
        'Alice would lose 79 happiness units by sitting next to Carol.',
        'Alice would lose 2 happiness units by sitting next to David.',
        'Bob would gain 83 happiness units by sitting next to Alice.',
        'Bob would lose 7 happiness units by sitting next to Carol.',
        'Bob would lose 63 happiness units by sitting next to David.',
        'Carol would lose 62 happiness units by sitting next to Alice.',
        'Carol would gain 60 happiness units by sitting next to Bob.',
        'Carol would gain 55 happiness units by sitting next to David.',
        'David would gain 46 happiness units by sitting next to Alice.',
        'David would lose 7 happiness units by sitting next to Bob.',
        'David would gain 41 happiness units by sitting next to Carol.',
    ]
    assert first(data) == 330


def test_M_2():
    data = [
        'Alice would gain 54 happiness units by sitting next to Bob.',
        'Alice would lose 79 happiness units by sitting next to Carol.',
        'Alice would lose 2 happiness units by sitting next to David.',
        'Bob would gain 83 happiness units by sitting next to Alice.',
        'Bob would lose 7 happiness units by sitting next to Carol.',
        'Bob would lose 63 happiness units by sitting next to David.',
        'Carol would lose 62 happiness units by sitting next to Alice.',
        'Carol would gain 60 happiness units by sitting next to Bob.',
        'Carol would gain 55 happiness units by sitting next to David.',
        'David would gain 46 happiness units by sitting next to Alice.',
        'David would lose 7 happiness units by sitting next to Bob.',
        'David would gain 41 happiness units by sitting next to Carol.',
    ]
    assert second(data) == 286


def test_N_1():
    data = [
        (
            'Comet can fly 14 km/s for 10 seconds, '
            'but then must rest for 127 seconds.'
        ),
        (
            'Dancer can fly 16 km/s for 11 seconds, '
            'but then must rest for 162 seconds.'
        )
    ]
    assert reindeer_olympics(data, 1000) == 1120


def test_N_2():
    data = [
        (
            'Comet can fly 14 km/s for 10 seconds, '
            'but then must rest for 127 seconds.'
        ),
        (
            'Dancer can fly 16 km/s for 11 seconds, '
            'but then must rest for 162 seconds.'
        )
    ]
    assert reindeer_olympics_2(data, 1000) == 689


def test_O():
    data = [
        'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
        'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
    ]
    assert best_combination(data, False) == 62842880
    assert best_combination(data, True) == 57600000


def test_P():
    sues = [
        'Sue 1: children: 1, cars: 8, vizslas: 7',
        'Sue 2: akitas: 10, perfumes: 10, children: 5',
        'Sue 3: cars: 5, pomeranians: 4, vizslas: 1',
        'Sue 4: cars: 5, pomeranians: 3, cats: 3',
        'Sue 5: goldfish: 5, children: 8, perfumes: 3',
        'Sue 6: vizslas: 2, akitas: 7, perfumes: 6',
        'Sue 7: vizslas: 0, akitas: 1, perfumes: 2',
        'Sue 8: perfumes: 8, cars: 4, goldfish: 10',
        'Sue 9: perfumes: 7, children: 2, cats: 1',
        'Sue 10: pomeranians: 3, goldfish: 10, trees: 10',
    ]
    cars = 5
    cats = 2
    pomeranians = 4
    vizslas = 1

    assert find_sue(
        analize_sue(sues),
        children=None,
        cats=cats,
        samoyeds=None,
        pomeranians=pomeranians,
        akitas=None,
        vizslas=vizslas,
        goldfish=None,
        trees=None,
        cars=cars,
        perfumes=None,
        task_1=True
    ) == 3

    assert find_sue(
        analize_sue(sues),
        children=None,
        cats=cats,
        samoyeds=None,
        pomeranians=pomeranians,
        akitas=None,
        vizslas=vizslas,
        goldfish=None,
        trees=None,
        cars=cars,
        perfumes=None,
        task_1=False
    ) == 4


def test_Q_1():
    data = [20, 15, 10, 5, 5]
    assert fill_refregirator(data, target_volume=25) == 4


def test_Q_2():
    data = [20, 15, 10, 5, 5]
    assert min_needed(data, target=25) == 3


def test_R_1():
    data = [
        ['.', '#', '.', '#', '.', '#'],
        ['.', '.', '.', '#', '#', '.'],
        ['#', '.', '.', '.', '.', '#'],
        ['.', '.', '#', '.', '.', '.'],
        ['#', '.', '#', '.', '.', '#'],
        ['#', '#', '#', '#', '.', '.']
    ]

    expected_1 = [
        ['.', '.', '#', '#', '.', '.'],
        ['.', '.', '#', '#', '.', '#'],
        ['.', '.', '.', '#', '#', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['#', '.', '.', '.', '.', '.'],
        ['#', '.', '#', '#', '.', '.']
    ]

    expected_2 = [
        ['.', '.', '#', '#', '#', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '#', '#', '#', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '#', '.', '.', '.', '.'],
        ['.', '#', '.', '.', '.', '.']
    ]

    expected_3 = [
        ['.', '.', '.', '#', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '#', '.', '.'],
        ['.', '.', '#', '#', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
    ]

    expected_4 = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '#', '#', '.', '.'],
        ['.', '.', '#', '#', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
    ]

    assert swap_light(data, False) == expected_1
    assert swap_light(expected_1, False) == expected_2
    assert swap_light(expected_2, False) == expected_3
    assert swap_light(expected_3, False) == expected_4


def test_R_2():
    data = [
        ['#', '#', '.', '#', '.', '#'],
        ['.', '.', '.', '#', '#', '.'],
        ['#', '.', '.', '.', '.', '#'],
        ['.', '.', '#', '.', '.', '.'],
        ['#', '.', '#', '.', '.', '#'],
        ['#', '#', '#', '#', '.', '#']
    ]

    expected_1 = [
        ['#', '.', '#', '#', '.', '#'],
        ['#', '#', '#', '#', '.', '#'],
        ['.', '.', '.', '#', '#', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['#', '.', '.', '.', '#', '.'],
        ['#', '.', '#', '#', '#', '#']
    ]

    expected_2 = [
        ['#', '.', '.', '#', '.', '#'],
        ['#', '.', '.', '.', '.', '#'],
        ['.', '#', '.', '#', '#', '.'],
        ['.', '.', '.', '#', '#', '.'],
        ['.', '#', '.', '.', '#', '#'],
        ['#', '#', '.', '#', '#', '#']
    ]

    expected_3 = [
        ['#', '.', '.', '.', '#', '#'],
        ['#', '#', '#', '#', '.', '#'],
        ['.', '.', '#', '#', '.', '#'],
        ['.', '.', '.', '.', '.', '.'],
        ['#', '#', '.', '.', '.', '.'],
        ['#', '#', '#', '#', '.', '#']
    ]

    expected_4 = [
        ['#', '.', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '#'],
        ['.', '.', '.', '#', '.', '.'],
        ['.', '#', '#', '.', '.', '.'],
        ['#', '.', '.', '.', '.', '.'],
        ['#', '.', '#', '.', '.', '#']
    ]

    assert swap_light(data, True) == expected_1
    assert swap_light(expected_1, True) == expected_2
    assert swap_light(expected_2, True) == expected_3
    assert swap_light(expected_3, True) == expected_4


def test_Y():
    assert build_graph(6, 1) == 33071741


def test_S_1():
    data = [
        'e => H',
        'e => O',
        'H => HO',
        'H => OH',
        'O => HH',
        'HOH'
    ]
    assert medicine_for_Rudolpf(data) == 4

    data = [
        'e => H',
        'e => O',
        'H => HO',
        'H => OH',
        'O => HH',
        'HOHOHO'
    ]
    assert medicine_for_Rudolpf(data) == 7


def test_S_2():
    data = [
        'e => H',
        'e => O',
        'H => HO',
        'H => OH',
        'O => HH',
        'HOH'
    ]
    assert medicine_for_Rudolpf_2(data) == 3

    data = [
        'e => H',
        'e => O',
        'H => HO',
        'H => OH',
        'O => HH',
        'HOHOHO'
    ]
    assert medicine_for_Rudolpf_2(data) == 6


def test_T_1():
    assert infinite_elves_and_infinite_houses(1) == 10
    assert infinite_elves_and_infinite_houses(2) == 30
    assert infinite_elves_and_infinite_houses(3) == 40
    assert infinite_elves_and_infinite_houses(4) == 70
    assert infinite_elves_and_infinite_houses(5) == 60
    assert infinite_elves_and_infinite_houses(6) == 120
    assert infinite_elves_and_infinite_houses(7) == 80
    assert infinite_elves_and_infinite_houses(8) == 150
    assert infinite_elves_and_infinite_houses(9) == 130


def test_U():
    me = Player(base_hitpoints=8, base_damage=5, base_armor=5)
    enemy = Player(base_hitpoints=12, base_damage=7, base_armor=2)
    assert me.fight(enemy)


def test_W():
    data = [
        'inc a',
        'jio a, +2',
        'tpl a',
        'inc a',
    ]
    assert use_register(data) == 0
