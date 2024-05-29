# from D.solution import play_bingo, play_bingo_2
# from E.solution import hydrothermal_venture, hydrothermal_venture_2
# from F.solution import lanternfisf
# from G.solution import min_horizontal_aligment

# from J.solution import syntax_scoring

# from M_13.solution import transparent_origami

# from Q_17.solution import trick_shot


# def test_A():
#     pass

# def test_D_1():
#     actions = [
#         7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10,
#         16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1
#     ]

#     boards = [
#         [
#             [22, 13, 17, 11, 0],
#             [8, 2, 23, 4, 24],
#             [21, 9, 14, 16, 7],
#             [6, 10, 3, 18, 5],
#             [1, 12, 20, 15, 19]
#         ],
#         [
#             [3, 15, 0, 2, 22],
#             [9, 18, 13, 17, 5],
#             [19, 8, 7, 25, 23],
#             [20, 11, 10, 24, 4],
#             [14, 21, 16, 12, 6]
#         ],
#         [
#             [14, 21, 17, 24, 4],
#             [10, 16, 15,  9, 19],
#             [18, 8, 23, 26, 20],
#             [22, 11, 13, 6, 5],
#             [2, 0, 12, 3, 7]
#         ]
#     ]
#     assert play_bingo(actions, boards) == 4512


# def test_D_2():
#     actions = [
#         7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10,
#         16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1
#     ]

#     boards = [
#         [
#             [22, 13, 17, 11, 0],
#             [8, 2, 23, 4, 24],
#             [21, 9, 14, 16, 7],
#             [6, 10, 3, 18, 5],
#             [1, 12, 20, 15, 19]
#         ],
#         [
#             [3, 15, 0, 2, 22],
#             [9, 18, 13, 17, 5],
#             [19, 8, 7, 25, 23],
#             [20, 11, 10, 24, 4],
#             [14, 21, 16, 12, 6]
#         ],
#         [
#             [14, 21, 17, 24, 4],
#             [10, 16, 15,  9, 19],
#             [18, 8, 23, 26, 20],
#             [22, 11, 13, 6, 5],
#             [2, 0, 12, 3, 7]
#         ]
#     ]
#     assert play_bingo_2(actions, boards) == 1924


# def test_E_1():
#     data = [
#         '0,9 -> 5,9',
#         '8,0 -> 0,8',
#         '9,4 -> 3,4',
#         '2,2 -> 2,1',
#         '7,0 -> 7,4',
#         '6,4 -> 2,0',
#         '0,9 -> 2,9',
#         '3,4 -> 1,4',
#         '0,0 -> 8,8',
#         '5,5 -> 8,2',
#     ]
#     assert hydrothermal_venture(data) == 5


# def test_E_2():
#     data = [
#         '0,9 -> 5,9',
#         '8,0 -> 0,8',
#         '9,4 -> 3,4',
#         '2,2 -> 2,1',
#         '7,0 -> 7,4',
#         '6,4 -> 2,0',
#         '0,9 -> 2,9',
#         '3,4 -> 1,4',
#         '0,0 -> 8,8',
#         '5,5 -> 8,2',
#     ]
#     assert hydrothermal_venture_2(data) == 12


# def test_F():
#     initial_state = [3, 4, 3, 1, 2]
#     assert lanternfisf(initial_state, 18) == 26
#     assert lanternfisf(initial_state, 80) == 5934


# def test_G_1():
#     assert min_horizontal_aligment([16, 1, 2, 0, 4, 2, 7, 1, 2, 14]) == 37


# def test_G_2():
#     assert min_horizontal_aligment(
#         [16, 1, 2, 0, 4, 2, 7, 1, 2, 14], True
#     ) == 168


# def test_J():
#     data = [
#         '[({(<(())[]>[[{[]{<()<>>',
#         '[(()[<>])]({[<{<<[]>>(',
#         '{([(<{}[<>[]}>{[]{[(<()>',
#         '(((({<>}<{<{<>}{[]{[]{}',
#         '[[<[([]))<([[{}[[()]]]',
#         '[{[{({}]{}}([{[{{{}}([]',
#         '{<[[]]>}<{[{[{[]{()[[[]',
#         '[<(<(<(<{}))><([]([]()',
#         '<{([([[(<>()){}]>(<<{{',
#         '<{([{{}}[<[[[<>{}]]]>[]]',
#     ]
#     assert syntax_scoring(data) == (26397, 288957)


# def test_M():
#     data = [
#         '6,10\n',
#         '0,14\n',
#         '9,10\n',
#         '0,3\n',
#         '10,4\n',
#         '4,11\n',
#         '6,0\n',
#         '6,12\n',
#         '4,1\n',
#         '0,13\n',
#         '10,12\n',
#         '3,4\n',
#         '3,0\n',
#         '8,4\n',
#         '1,10\n',
#         '2,14\n',
#         '8,10\n',
#         '9,0\n',
#         '\n',
#         'fold along y=7\n',
#         'fold along x=5\n'
#     ]
#     assert transparent_origami(data) == 17


# def test_Q():
#     data = 'target area: x=20..30, y=-10..-5'
#     assert trick_shot(data) == (45, 112)
