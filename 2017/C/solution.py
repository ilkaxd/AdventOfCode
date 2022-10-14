def spiral_memory(data):
    """
    Числа хранятся по спирали в формате
    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...
    Необходимо найти манхетоновское расстояние
    от 1 до целевого числа
    """
    grid = {}
    X, Y = 0, 0

    directions = ['R', 'U', 'L', 'D']
    direction_i = 0

    value = 1

    grid[(X, Y)] = value

    while value < data:
        direction = directions[direction_i]
        value += 1
        if direction == 'R':
            X += 1
            grid[(X, Y)] = value
            if grid.get((X, Y + 1)) is None:
                direction_i += 1
        elif direction == 'U':
            Y += 1
            grid[(X, Y)] = value
            if grid.get((X - 1, Y)) is None:
                direction_i += 1
        elif direction == 'L':
            X -= 1
            grid[(X, Y)] = value
            if grid.get((X, Y - 1)) is None:
                direction_i += 1
        elif direction == 'D':
            Y -= 1
            grid[(X, Y)] = value
            if grid.get((X + 1, Y)) is None:
                direction_i = 0

    for key, value in grid.items():
        if value == data:
            return abs(key[0]) + abs(key[1])


def get_value(X, Y, panel):
    left_down = panel.get((X - 1, Y - 1), 0)
    left_min = panel.get((X - 1, Y), 0)
    left_up = panel.get((X - 1, Y + 1), 0)

    mid_down = panel.get((X, Y - 1), 0)
    mid_up = panel.get((X, Y + 1), 0)

    right_down = panel.get((X + 1, Y - 1), 0)
    right_mid = panel.get((X + 1, Y), 0)
    right_up = panel.get((X + 1, Y + 1), 0)

    return (
        left_down + left_min + left_up +
        mid_down + mid_up +
        right_down + right_mid + right_up
    )


def spiral_memory_2(data):
    """
    Порядок заполнения аналогичен предыдущей задаче,
    но следующее вставляемое число вычисляется как сумма
    ближайших ячеек
    Ищем первое число, которое больше входного
    """
    grid = {}
    X, Y = 0, 0

    directions = ['R', 'U', 'L', 'D']
    direction_i = 0

    value = 1

    grid[(X, Y)] = value

    while value <= data:
        direction = directions[direction_i]
        if direction == 'R':
            X += 1
            value = get_value(X, Y, grid)
            grid[(X, Y)] = value
            if grid.get((X, Y + 1)) is None:
                direction_i += 1
        elif direction == 'U':
            Y += 1
            value = get_value(X, Y, grid)
            grid[(X, Y)] = value
            if grid.get((X - 1, Y)) is None:
                direction_i += 1
        elif direction == 'L':
            X -= 1
            value = get_value(X, Y, grid)
            grid[(X, Y)] = value
            if grid.get((X, Y - 1)) is None:
                direction_i += 1
        elif direction == 'D':
            Y -= 1
            value = get_value(X, Y, grid)
            grid[(X, Y)] = value
            if grid.get((X + 1, Y)) is None:
                direction_i = 0

    return value


if __name__ == '__main__':
    data = 361527
    print(spiral_memory(data))
    print(spiral_memory_2(data))
