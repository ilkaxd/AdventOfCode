# from A_01.solution import (
#     calculate_fuel_requered,
#     calculate_recursion_fuel_requered
# )

# from B_02.solution import (
#     program_alarm,
# )

# from C_03.solution import (
#     crossed_wires,
#     crossed_wires_2
# )

# from D_04.solution import (
#     double_values,
#     double_values_2,
#     increace_numbers
# )

# from E_05.solution import TEST_actions
# from F_06.solution import OrbitMap

# from H_08.solution import split_by_layers

# from L_12.solution import n_body_problem


# def test_A_1():
#     assert calculate_fuel_requered(12) == 2
#     assert calculate_fuel_requered(14) == 2
#     assert calculate_fuel_requered(1969) == 654
#     assert calculate_fuel_requered(100756) == 33583


# def test_A_2():
#     assert calculate_recursion_fuel_requered(12) == 2
#     assert calculate_recursion_fuel_requered(1969) == 966
#     assert calculate_recursion_fuel_requered(100756) == 50346


# def test_B_1():
#     assert program_alarm([
#         1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50
#     ]) == 3500


# def test_C_1():
#     data_1 = [
#         [('R', 8), ('U', 5), ('L', 5), ('D', 3)],
#         [('U', 7), ('R', 6), ('D', 4), ('L', 4)]
#     ]

#     data_2 = [
#         [('R', 75), ('D', 30), ('R', 83), ('U', 83), ('L', 12), ('D', 49), ('R', 71), ('U', 7), ('L', 72)],
#         [('U', 62), ('R', 66), ('U', 55), ('R', 34), ('D', 71), ('R', 55), ('D', 58), ('R', 83)]
#     ]

#     data_3 = [
#         [('R', 98), ('U', 47), ('R', 26), ('D', 63), ('R', 33), ('U', 87), ('L', 62), ('D', 20), ('R', 33), ('U', 53), ('R', 51)],
#         [('U', 98), ('R', 91), ('D', 20), ('R', 16), ('D', 67), ('R', 40), ('U', 7), ('R', 15), ('U', 6), ('R', 7)]
#     ]

#     assert crossed_wires(data_1) == 6
#     assert crossed_wires(data_2) == 159
#     assert crossed_wires(data_3) == 135


# def test_C_2():
#     data_1 = [
#         [('R', 8), ('U', 5), ('L', 5), ('D', 3)],
#         [('U', 7), ('R', 6), ('D', 4), ('L', 4)]
#     ]

#     data_2 = [
#         [('R', 75), ('D', 30), ('R', 83), ('U', 83), ('L', 12), ('D', 49), ('R', 71), ('U', 7), ('L', 72)],
#         [('U', 62), ('R', 66), ('U', 55), ('R', 34), ('D', 71), ('R', 55), ('D', 58), ('R', 83)]
#     ]

#     data_3 = [
#         [('R', 98), ('U', 47), ('R', 26), ('D', 63), ('R', 33), ('U', 87), ('L', 62), ('D', 20), ('R', 33), ('U', 53), ('R', 51)],
#         [('U', 98), ('R', 91), ('D', 20), ('R', 16), ('D', 67), ('R', 40), ('U', 7), ('R', 15), ('U', 6), ('R', 7)]
#     ]

#     assert crossed_wires_2(data_1) == 30
#     assert crossed_wires_2(data_2) == 610
#     assert crossed_wires_2(data_3) == 410


# def test_D():
#     value = 112233
#     assert double_values(value) and increace_numbers(value)
#     value = 223450
#     assert double_values(value) and not increace_numbers(value)
#     value = 123789
#     assert not double_values(value) and increace_numbers(value)
#     assert double_values_2(112233)
#     assert not double_values_2(123444)
#     assert double_values_2(111122)


# def test_E():
#     data = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
#     assert TEST_actions(data, 7) == 0
#     assert TEST_actions(data, 8) == 1
#     assert TEST_actions(data, 9) == 0

#     data = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
#     assert TEST_actions(data, 7) == 1
#     assert TEST_actions(data, 8) == 0
#     assert TEST_actions(data, 9) == 0

#     data = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
#     assert TEST_actions(data, 7) == 0
#     assert TEST_actions(data, 8) == 1
#     assert TEST_actions(data, 9) == 0

#     data = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
#     assert TEST_actions(data, 7) == 1
#     assert TEST_actions(data, 8) == 0
#     assert TEST_actions(data, 9) == 0

#     data = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
#     assert TEST_actions(data, 0) == 0
#     assert TEST_actions(data, 2) == 1

#     data = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
#     assert TEST_actions(data, 0) == 0
#     assert TEST_actions(data, 2) == 1

#     data = [
#         3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
#         1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
#         999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
#     ]
#     assert TEST_actions(data, 7) == 999
#     assert TEST_actions(data, 8) == 1000
#     assert TEST_actions(data, 9) == 1001


# def test_F_1():
#     data = [
#         'COM)B',
#         'B)C',
#         'C)D',
#         'D)E',
#         'E)F',
#         'B)G',
#         'G)H',
#         'D)I',
#         'E)J',
#         'J)K',
#         'K)L',
#     ]
#     assert OrbitMap(data) == 42


# def test_H():
#     data = '123456789012'
#     assert split_by_layers(data, 3, 2) == 1


# def test_L():
#     data = [
#         '<x=-1, y=0, z=2>',
#         '<x=2, y=-10, z=-7>',
#         '<x=4, y=-8, z=8>',
#         '<x=3, y=5, z=-1>'
#     ]
#     assert n_body_problem(data, 10) == 179
#     data = [
#         '<x=-8, y=-10, z=0>',
#         '<x=5, y=5, z=10>',
#         '<x=2, y=-7, z=3>',
#         '<x=9, y=-8, z=-3>'
#     ]
#     assert n_body_problem(data, 100) == 1940