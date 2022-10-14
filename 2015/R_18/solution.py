import copy


def load_data():
    with open(r'2015\R_18\input.txt') as f:
        return [list(x) for x in f.read().split('\n') if x != '']


def get_grid_value(value):
    if value == '#':
        return 1
    return 0


def swap_light(grid, fix_corner):
    """
    Имеется сетка, 100 х 100, в которой
        - # - соответствует 1
        - . - соответствует 0
    Следующее состояние сетки зависит от суммы состояний соседей (X)
    и текущего состояния
    Текущее состояние:
        - #:
            - перейдёт в #, если X = 2 или 3
            - перейдёт в .
        - .:
            - перейдёт в #, если X = 3
            - перейдёт в .
    Во второй части угловые элементы сетки равны # и не выключаются
    """
    heigth = len(grid)
    width = len(grid[0])

    if fix_corner:
        grid[0][0] = '#'
        grid[heigth - 1][0] = '#'
        grid[0][width - 1] = '#'
        grid[heigth - 1][width - 1] = '#'
    result = copy.deepcopy(grid)
    for row in range(heigth):
        for column in range(width):
            if fix_corner:
                if (
                    (row == 0 and column == 0)
                    or
                    (row == heigth - 1 and column == 0)
                    or
                    (row == 0 and column == width - 1)
                    or
                    (row == heigth - 1 and column == width - 1)
                ):
                    continue
            cell_value = get_grid_value(grid[row][column])
            neighbours = 0
            for i in range(max(row - 1, 0), min(row + 1 + 1, heigth)):
                for j in range(max(column - 1, 0), min(column + 1 + 1, width)):
                    if i == row and j == column:
                        continue
                    neighbours += get_grid_value(grid[i][j])
            if cell_value == 1:
                if neighbours == 2 or neighbours == 3:
                    result[row][column] = '#'
                else:
                    result[row][column] = '.'
            else:
                if neighbours == 3:
                    result[row][column] = '#'
                else:
                    result[row][column] = '.'
    return result


def swap_light_repeatedly(data, n, second=False):
    global states
    for _ in range(n):
        data = swap_light(data, second)
    result = 0
    for row in data:
        for value in row:
            result += get_grid_value(value)
    return result


if __name__ == '__main__':
    data = load_data()
    print(swap_light_repeatedly(data, 100))
    print(swap_light_repeatedly(data, 100, True))
