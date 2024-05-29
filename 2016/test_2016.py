# from A_01.solution import findMinDistance, findFirstSamePoints
# from B_02.solution import bathroom_security, pretentious_panel
# from C_03.solution import is_triangle_possible, count_available_triangles_2
# from D_04.solution import is_real_room, decrypt
# from E_05.solution import find_password, find_password_2
# from F_06.solution import find_common_values, find_least_common_values
# from G_07.solution import support_TLS, support_SSL
# from H_08.solution import Screen
# from I_09.solution import explosives, explosives_2
# from J_10.solution import balance_bots

# from L_12.solution import make_instructions
# from M_13.solution import Maze
# from N_14.solution import one_time_pad
# from O_15.solution import timing_is_everything
# from P_16.solution import dragon_checksum
# from Q_17.solution import two_steps_forward
# from R_18.solution import like_rogue
# from S_19.solution import elephant_named_joseph, elephant_named_joseph_2
# from T_20.solution import firewall_rules
# from U_21.solution import scrambled_letter


# def test_A_1():
#     assert findMinDistance(['R2', 'L3']) == 5
#     assert findMinDistance(['R2', 'R2', 'R2']) == 2
#     assert findMinDistance(['R5', 'L5', 'R5', 'R3']) == 12


# def test_A_2():
#     assert findFirstSamePoints(['R8', 'R4', 'R4', 'R8']) == 4


# def test_B_1():
#     data = [
#         'ULL',
#         'RRDDD',
#         'LURDL',
#         'UUUUD',
#     ]
#     assert bathroom_security(data) == '1985'


# def test_B_2():
#     data = [
#         'ULL',
#         'RRDDD',
#         'LURDL',
#         'UUUUD',
#     ]
#     assert bathroom_security(data, pretentious_panel) == '5DB3'


# def test_C_1():
#     data = [5, 10, 14]
#     assert is_triangle_possible(*data)


# def test_C_2():
#     data = [
#         [101, 301, 501],
#         [102, 302, 502],
#         [103, 303, 503],
#         [201, 401, 601],
#         [202, 402, 602],
#         [203, 403, 603]
#     ]
#     assert count_available_triangles_2(data) == 6


# def test_D_1():
#     assert is_real_room('aaaaa-bbb-z-y-x-123[abxyz]')[0]
#     assert is_real_room('a-b-c-d-e-f-g-h-987[abcde]')[0]
#     assert is_real_room('not-a-real-room-404[oarel]')[0]
#     assert not is_real_room('totally-real-room-200[decoy]')[0]


# def test_D_2():
#     data = 'qzmt-zixmtkozy-ivhz-343'
#     assert decrypt(data)[0] == 'very encrypted name'


# def test_E_1():
#     data = 'abc'
#     assert find_password(data) == '18f47a30'


# def test_E_2():
#     data = 'abc'
#     assert find_password_2(data) == '05ace8e3'


# def test_F_1():
#     data = [
#         'eedadn',
#         'drvtee',
#         'eandsr',
#         'raavrd',
#         'atevrs',
#         'tsrnev',
#         'sdttsa',
#         'rasrtv',
#         'nssdts',
#         'ntnada',
#         'svetve',
#         'tesnvt',
#         'vntsnd',
#         'vrdear',
#         'dvrsen',
#         'enarar',
#     ]
#     assert find_common_values(data) == 'easter'


# def test_F_2():
#     data = [
#         'eedadn',
#         'drvtee',
#         'eandsr',
#         'raavrd',
#         'atevrs',
#         'tsrnev',
#         'sdttsa',
#         'rasrtv',
#         'nssdts',
#         'ntnada',
#         'svetve',
#         'tesnvt',
#         'vntsnd',
#         'vrdear',
#         'dvrsen',
#         'enarar',
#     ]
#     assert find_least_common_values(data) == 'advent'


# def test_G_1():
#     data = [
#         ('abba[mnop]qrst', True),
#         ('abcd[bddb]xyyx', False),
#         ('aaaa[qwer]tyui', False), 
#         ('ioxxoj[asdfgh]zxcvbn', True),
#     ]
#     for row, expected in data:
#         assert support_TLS(row) == expected


# def test_G_2():
#     data = [
#         ('aba[bab]xyz', True),
#         ('xyx[xyx]xyx', False),
#         ('aaa[kek]eke', True),
#         ('zazbz[bzb]cdb', True)
#     ]
#     for row, expected in data:
#         assert support_SSL(row) == expected


# def test_H():
#     screen = Screen(7, 3)
#     screen.parse_string('rect 3x2')
#     screen.parse_string('rotate column x=1 by 1')
#     screen.parse_string('rotate row y=0 by 4')
#     screen.parse_string('rotate column x=1 by 1')
#     expected = '\n'.join([
#         '. # . . # . #',
#         '# . # . . . .',
#         '. # . . . . .',
#     ])
#     assert str(screen) == expected


# def test_I_1():
#     data = [
#         ('ADVENT', 'ADVENT', 6),
#         ('A(1x5)BC', 'ABBBBBC', 7),
#         ('(3x3)XYZ', 'XYZXYZXYZ', 9),
#         ('A(2x2)BCD(2x2)EFG', 'ABCBCDEFEFG', 11),
#         ('(6x1)(1x3)A', '(1x3)A', 6),
#         ('X(8x2)(3x3)ABCY', 'X(3x3)ABC(3x3)ABCY', 18)
#     ]

#     for value, expected, expected_len in data:
#         result = explosives(value)
#         assert result == expected
#         assert len(result) == expected_len


# def test_I_2():
#     data = [
#         ('(3x3)XYZ', 9),
#         ('X(8x2)(3x3)ABCY', 20),
#         ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241920),
#         ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445)
#     ]
#     for value, expected in data:
#         result = explosives_2(value)
#         assert result == expected


# def test_J():
#     data = [
#         'value 5 goes to bot 2',
#         'bot 2 gives low to bot 1 and high to bot 0',
#         'value 3 goes to bot 1',
#         'bot 1 gives low to output 1 and high to bot 0',
#         'bot 0 gives low to output 2 and high to output 0',
#         'value 2 goes to bot 2',
#     ]

#     assert balance_bots(data, 2, 5)[0] == 2


# def test_K():
#     pass


# def test_L():
#     data = [
#         'cpy 41 a',
#         'inc a',
#         'inc a',
#         'dec a',
#         'jnz a 2',
#         'dec a',
#     ]
#     assert make_instructions(data) == 42


# def test_M_1():
#     assert Maze(
#         x=1, y=1,
#         favorite_number=10,
#         visited=[], steps=0,
#         target_x=7, target_y=4
#     ) == 11


# def test_N_1():
#     data = 'abc'
#     assert one_time_pad(data) == 22728


# def test_N_2():
#     data = 'abc'
#     assert one_time_pad(data, 2016) == 22551


# def test_O_1():
#     data = [
#         'Disc #1 has 5 positions; at time=0, it is at position 4.',
#         'Disc #2 has 2 positions; at time=0, it is at position 1.'
#     ]
#     assert timing_is_everything(data) == 5


# def test_P():
#     data = [1, 0, 0, 0, 0]
#     assert dragon_checksum(data, 20) == '01100'


# def test_Q():
#     data = 'ihgpwlah'
#     assert two_steps_forward(data) == ('DDRRRD', 370)
#     data = 'kglvqrro'
#     assert two_steps_forward(data) == ('DDUDRLRRUDRD', 492)
#     data = 'ulqzkmiv'
#     assert two_steps_forward(data) == ('DRURDRUDDLLDLUURRDULRLDUUDDDRR', 830)


# def test_R():
#     data = '.^^.^.^^^^'
#     assert like_rogue(data, 10) == 38


# def test_S_1():
#     assert elephant_named_joseph(5) == 3


# def test_S_2():
#     assert elephant_named_joseph_2(5) == 2


# def test_T():
#     data = [
#         '5-8',
#         '0-2',
#         '4-7'
#     ]
#     assert firewall_rules(data, 0, 9) == (3, 2)


# def test_U():
#     password = 'abcde'
#     data = [
#         'swap position 4 with position 0',
#         'swap letter d with letter b',
#         'reverse positions 0 through 4',
#         'rotate left 1 step',
#         'move position 1 to position 4',
#         'move position 3 to position 0',
#         'rotate based on position of letter b',
#         'rotate based on position of letter d'
#     ]
#     result = scrambled_letter(password, data)
#     assert result == 'decab'
#     assert scrambled_letter(result, data, True) == password
