from collections import defaultdict
import matplotlib.pyplot as plt


def load_data():
    with open((r'2021\M_13\input.txt')) as f:
        return f.readlines()


def split_data(data):
    coordinates = []
    instructions = []
    for row in data:
        if row == '\n':
            continue
        elif row.startswith('fold'):
            row = row.replace('fold along ', '').rstrip('\n')
            direction, value = row.split('=')
            instructions.append((direction, int(value)))
        else:
            row = row.rstrip('\n')
            coordinates.append(tuple(map(int, row.split(','))))
    return coordinates, instructions


def get_max_values(grid):
    target = [x for x, y in grid.items() if y]
    max_x = max(target, key=lambda x: x[0])[0]
    max_y = max(target, key=lambda x: x[1])[1]
    return max_x, max_y


def print_grid(grid):
    max_x, max_y = get_max_values(grid)
    result = []
    for y in range(max_y + 1):
        row = []
        for x in range(max_x + 1):
            if grid[(x, y)]:
                # print('x', end='')
                row.append(1)
            else:
                # print(' ', end='')
                row.append(0)
        result.append(row)
        # print()
    plt.imshow(result)
    plt.show()


def fold(grid, x_line=0, y_line=0):
    max_x, max_y = get_max_values(grid)
    if x_line != 0:
        for y in range(max_y + 1):
            for x in range(x_line, max_x + 1):
                if grid[(x, y)]:
                    grid[(x, y)] = False
                    grid[(x_line - (x - x_line), y)] = True

    else:
        for y in range(y_line, max_y + 1):
            for x in range(max_x + 1):
                if grid[(x, y)]:
                    grid[(x, y)] = False
                    grid[(x, y_line - (y - y_line))] = True


def transparent_origami(data, show=False):
    """
    Имеется набор точек и набор инструкций
    Инструкции сворачивают пространство вдоль
    указанной линии.
    Считаем количество закрашенных точек после
    первого сворачивания
    И смотрим на результат после всех сворачиваний
    """
    coordinates, instructions = split_data(data)
    grid = defaultdict(bool)
    for coordinate in coordinates:
        grid[coordinate] = True

    results = []
    for direction, value in instructions:
        if direction == 'x':
            fold(grid, value, 0)
        else:
            fold(grid, 0, value)
        results.append(sum(grid.values()))
    if show:
        print_grid(grid)
    return results[0]


if __name__ == '__main__':
    data = load_data()
    print(transparent_origami(data, True))
