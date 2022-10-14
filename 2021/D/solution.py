import copy


class Point:
    def __init__(self, value):
        self.value = value
        self.is_marked = False

    def __str__(self) -> str:
        return f'{self.value} ({self.is_marked})'

    def __repr__(self) -> str:
        return self.__str__()


def load_data():
    with open(r'2021\D\input.txt') as f:
        actions = list(map(int, f.readline().split(',')))
        boards = [
            board.split('\n')
            for board in f.read().split('\n\n')
        ]
        for i in range(len(boards)):
            board = boards[i]
            parsed_board = []
            for row in board:
                if row != '':
                    parsed_row = []
                    for value in row.split():
                        parsed_row.append(int(value))
                    parsed_board.append(parsed_row)
            boards[i] = parsed_board
        return actions, boards


def set_value(board, value):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if value == board[i][j].value:
                board[i][j].is_marked = True


def is_wining_board(board):
    # По строкам
    for row in board:
        if all(point.is_marked for point in row):
            return True
    # По столбцам
    for j in range(len(board[0])):
        result = []
        for i in range(len(board)):
            result.append(board[i][j].is_marked)
        if all(result):
            return True
    return False


def calculate_unmarked(board):
    result = 0
    for row in board:
        for point in row:
            if not point.is_marked:
                result += point.value
    return result


def play_bingo(actions, boards):
    '''
    Играем в бинго, доска является выйгрышной,
    если по вертикали или горизонтали выбраны все цифры
    Результат:
        сумма всех неотмеченных цифр * число,
        на котором сработало бинго
    '''
    for i in range(len(boards)):
        for row in range(len(boards[i])):
            for column in range(len(boards[i][row])):
                value = boards[i][row][column]
                boards[i][row][column] = Point(value)

    for action in actions:
        for i in range(len(boards)):
            set_value(boards[i], action)
            if is_wining_board(boards[i]):
                return calculate_unmarked(boards[i]) * action


def play_bingo_2(actions, boards):
    '''
    Ищем последнюю доску
    '''
    for i in range(len(boards)):
        for row in range(len(boards[i])):
            for column in range(len(boards[i][row])):
                value = boards[i][row][column]
                boards[i][row][column] = Point(value)

    winning = dict((i, False) for i in range(len(boards)))

    for action in actions:
        for i in range(len(boards)):
            if winning[i]:
                continue
            set_value(boards[i], action)
            if is_wining_board(boards[i]):
                winning[i] = True
                if all(winning.values()):
                    return calculate_unmarked(boards[i]) * action


if __name__ == '__main__':
    actions, boards = load_data()
    print(play_bingo(actions, copy.deepcopy(boards)))
    print(play_bingo_2(actions, copy.deepcopy(boards)))
