# from A.solution import (
#     inverse_captcha,
#     inverse_captcha_2
# )

# from B.solution import (
#     corruption_checksum,
#     corruption_checksum_2
# )

# from C.solution import (
#     spiral_memory,
#     spiral_memory_2
# )

# from D.solution import (
#     passphrases_count,
#     check_anagram
# )

# from E.solution import (
#     twisty_trampolines,
#     twisty_trampolines_2
# )

# from F.solution import (
#     memory_relocation,
#     memory_relocation_2,
# )

# from G.solution import (
#     find_tree_root,
#     tree_balance
# )

# from H.solution import (
#     you_like_registers,
#     you_like_registers_2
# )

# from I.solution import (
#     stream_processing,
#     stream_processing_2
# )

# from J.solution import (
#     knot_hash,

# )

# from M_13.solution import packet_scanners

# from O_15.solution import dueling_generators, dueling_generators_2
# from P_16.solution import permutation_promenade_сyclical

# def test_A_1():
#     assert inverse_captcha([1, 1, 2, 2]) == 3
#     assert inverse_captcha([1, 1, 1, 1]) == 4
#     assert inverse_captcha([1, 2, 3, 4]) == 0
#     assert inverse_captcha([9, 1, 2, 1, 2, 1, 2, 9]) == 9


# def test_A_2():
#     assert inverse_captcha_2([1, 2, 1, 2]) == 6
#     assert inverse_captcha_2([1, 2, 2, 1]) == 0
#     assert inverse_captcha_2([1, 2, 3, 4, 2, 5]) == 4
#     assert inverse_captcha_2([1, 2, 3, 1, 2, 3]) == 12
#     assert inverse_captcha_2([1, 2, 1, 3, 1, 4, 1, 5]) == 4


# def test_B_1():
#     data = [
#         [5, 1, 9, 5],
#         [7, 5, 3],
#         [2, 4, 6, 8]
#     ]
#     assert corruption_checksum(data) == 18


# def test_B_2():
#     data = [
#         [5, 9, 2, 8],
#         [9, 4, 7, 3],
#         [3, 8, 6, 5]
#     ]
#     assert corruption_checksum_2(data) == 9


# def test_C_1():
#     assert spiral_memory(1) == 0
#     assert spiral_memory(12) == 3
#     assert spiral_memory(23) == 2
#     assert spiral_memory(1024) == 31


# def test_C_2():
#     assert spiral_memory_2(1) == 2
#     assert spiral_memory_2(2) == 4
#     assert spiral_memory_2(11) == 23
#     assert spiral_memory_2(351) == 362


# def test_D_1():
#     assert passphrases_count([
#         ['aa', 'bb', 'cc', 'dd', 'ee'],
#         ['aa', 'bb', 'cc', 'dd', 'aa'],
#         ['aa', 'bb', 'cc', 'dd', 'aaa']
#     ]) == 2


# def test_D_2():
#     assert check_anagram(['abcde', 'fghij'])
#     assert not check_anagram(['abcde', 'xyz', 'ecdab'])
#     assert check_anagram(['a', 'ab', 'abc', 'abd', 'abf', 'abj'])
#     assert check_anagram(['iiii', 'oiii', 'ooii', 'oooi', 'oooo'])
#     assert not check_anagram(['oiii', 'ioii', 'iioi', 'iiio'])


# def test_E_1():
#     assert twisty_trampolines([0, 3, 0, 1, -3]) == 5


# def test_E_2():
#     assert twisty_trampolines_2([0, 3, 0, 1, -3]) == 10


# def test_F_1():
#     assert memory_relocation([0, 2, 7, 0]) == 5


# def test_F_2():
#     assert memory_relocation_2([0, 2, 7, 0]) == 4


# def test_G_1():
#     data = [
#         'pbga (66)',
#         'xhth (57)',
#         'ebii (61)',
#         'havc (66)',
#         'ktlj (57)',
#         'fwft (72) -> ktlj, cntj, xhth',
#         'qoyq (66)',
#         'padx (45) -> pbga, havc, qoyq',
#         'tknk (41) -> ugml, padx, fwft',
#         'jptl (61)',
#         'ugml (68) -> gyxo, ebii, jptl',
#         'gyxo (61)',
#         'cntj (57)',
#     ]
#     assert find_tree_root(data) == 'tknk'


# def test_G_2():
#     data = [
#         'pbga (66)',
#         'xhth (57)',
#         'ebii (61)',
#         'havc (66)',
#         'ktlj (57)',
#         'fwft (72) -> ktlj, cntj, xhth',
#         'qoyq (66)',
#         'padx (45) -> pbga, havc, qoyq',
#         'tknk (41) -> ugml, padx, fwft',
#         'jptl (61)',
#         'ugml (68) -> gyxo, ebii, jptl',
#         'gyxo (61)',
#         'cntj (57)',
#     ]
#     assert tree_balance(data) == 60

#     data = [
#         'pbga (66)',
#         'xhth (67)',
#         'ebii (61)',
#         'havc (66)',
#         'ktlj (57)',
#         'fwft (72) -> ktlj, cntj, xhth',
#         'qoyq (76)',
#         'padx (45) -> pbga, havc, qoyq',
#         'tknk (41) -> ugml, padx, fwft',
#         'jptl (61)',
#         'ugml (68) -> gyxo, ebii, jptl',
#         'gyxo (61)',
#         'cntj (57)',
#     ]
#     assert tree_balance(data) == 70


# def test_H_1():
#     data = [
#         'b inc 5 if a > 1',
#         'a inc 1 if b < 5',
#         'c dec -10 if a >= 1',
#         'c inc -20 if c == 10',
#     ]
#     assert you_like_registers(data) == 1


# def test_H_2():
#     data = [
#         'b inc 5 if a > 1',
#         'a inc 1 if b < 5',
#         'c dec -10 if a >= 1',
#         'c inc -20 if c == 10',
#     ]
#     assert you_like_registers_2(data) == 10


# def test_I_1():
#     assert stream_processing('{}') == 1
#     assert stream_processing('{{{}}}') == 6
#     assert stream_processing('{{},{}}') == 5
#     assert stream_processing('{{{},{},{{}}}}') == 16
#     assert stream_processing('{<a>,<a>,<a>,<a>}') == 1
#     assert stream_processing('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
#     assert stream_processing('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
#     assert stream_processing('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3


# def test_I_2():
#     assert stream_processing_2('<>') == 0
#     assert stream_processing_2('<random characters>') == 17
#     assert stream_processing_2('<<<<>') == 3
#     assert stream_processing_2('<{!>}>') == 2
#     assert stream_processing_2('<!!>') == 0
#     assert stream_processing_2('<!!!>>') == 0
#     assert stream_processing_2('<{o"i!a,<{i<a>') == 10


# def test_M():
#     data = [
#         '0: 3',
#         '1: 2',
#         '4: 4',
#         '6: 4'
#     ]
#     assert packet_scanners(data) == (24, 10)


# def test_J_1():
#     inputs = list(range(5))
#     lengths = [3, 4, 1, 5]
#     assert knot_hash(inputs, lengths) == 12


# def test_O_1():
#     data = [65, 8921]
#     assert dueling_generators(*data, size=100_000) == 3


# def test_O_2():
#     data = [65, 8921]
#     assert dueling_generators_2(*data, size=100_000) == 7


# def test_P():
#     data = [
#         's1',
#         'x3/4',
#         'pe/b'
#     ]
#     size = 5
#     assert permutation_promenade_сyclical(data, size, 1) == 'baedc'
#     assert permutation_promenade_сyclical(data, size, 1_000_000_000) == 'abcde'


# def test_S():
#     data = [
#         [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#         [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', '+', '-', '-', '+', ' ', ' ', ' ', ' '],
#         [' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', '|', ' ', ' ', 'C', ' ', ' ', ' ', ' '],
#         [' ', 'F', '-', '-', '-', '|', '-', '-', '-', '-', 'E', '|', '-', '-', '+', ' '],
#         [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', '|', ' ', ' ', '|', ' ', ' ', 'D', ' '],
#         [' ', ' ', ' ', ' ', ' ', '+', 'B', '-', '+', ' ', ' ', '+', '-', '-', '+', ' '],
#         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#     ]
