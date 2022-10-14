from collections import defaultdict

def load_data():
    with open(r'2018\F_06\input.txt') as f:
        return [list(map(int, line.split(', '))) for line in f.readlines()]


def ChronalCoordinates(coordinates):
    '''
    Имеется набор координат, вычисляем для каждой точки
    манхетоновское расстояние, и присваиваем ей индекс с минимальным значением
    или ".", если имеются одинаковые минимальные расстояния
    нужно найти наибольшую замкнутую область, 
    '''
    grid = defaultdict(list)
    rows = [row for column, row in coordinates]
    columns = [column for column, row in coordinates]
    max_row = max(rows)
    min_row = min(rows)

    max_column = max(columns)
    min_column = min(columns)

    for i, (y, x) in enumerate(coordinates):
        for row in range(min_row, max_row + 1):
            for column in range(min_column, max_column + 1):
                grid[(row, column)].append(
                    (abs(row - x) + abs(column - y), i)
                )

    infinity = []

    for row in range(min_row, max_row + 1):
        for column in range(min_column, max_column + 1):
            grid[(row, column)] = sorted(
                grid[(row, column)], key=lambda x: x[0]
            )
            if grid[(row, column)][0][0] == grid[(row, column)][1][0]:
                grid[(row, column)] = (None,  '.')
            else:
                grid[(row, column)] = grid[(row, column)][0]
            if (
                (
                    row == min_row or
                    column == min_column or
                    row == max_row or
                    column == max_column
                ) and
                grid[(row, column)][1] != '.'
            ):
                infinity.append(grid[(row, column)][1])
    infinity.append('.')
    infinity = set(infinity)
    result = 0

    result = dict(
        (i, 0) for i in range(len(coordinates)) if i not in infinity
    )

    for row in range(min_row, max_row + 1):
        for column in range(min_column, max_column + 1):
            if grid[(row, column)][1] not in infinity:
                result[grid[(row, column)][1]] += 1

    return max(result.values())

def ChronalCoordinates_2(coordinates, threshold=10000):
    '''
    Для каждой точки вычисляем суммы манхетоновских расстояний
    и ищем область, в которой значение будет меньше порога
    '''
    grid = defaultdict(int)
    rows = [row for column, row in coordinates]
    columns = [column for column, row in coordinates]
    max_row = max(rows)
    min_row = min(rows)

    max_column = max(columns)
    min_column = min(columns)

    for (y, x) in coordinates:
        for row in range(min_row, max_row + 1):
            for column in range(min_column, max_column + 1):
                grid[(row, column)] += abs(row - x) + abs(column - y)
    result = 0
    for row in range(min_row, max_row + 1):
        for column in range(min_column, max_column + 1):
            if grid[(row, column)] < threshold:
                result += 1

    return result


if __name__ == '__main__':
    data = load_data()
    # data = [
    #     [1, 1],
    #     [1, 6],
    #     [8, 3],
    #     [3, 4],
    #     [5, 5],
    #     [8, 9]
    # ]
    # print(ChronalCoordinates(data))
    print(ChronalCoordinates_2(data))
