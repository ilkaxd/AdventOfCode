def load_data():
    with open(r'2016\R_18\input.txt') as f:
        return f.readline().rstrip('\n')


def is_a_trap(left, center, right):
    if left and center and not right:
        return True
    if center and right and not left:
        return True
    if left and not center and not right:
        return True
    if right and not left and not center:
        return True
    return False


def like_rogue(data, size=40):
    '''
    Задана первая строка сетки
    ячейки в сетке могут быть ловушкой (^)
    или чистой (.)
    Значение в новой строке определяет по значением из
    предыдущей строки
    Считаем количество безопасных ячеек
    '''
    data = [True if x == '^' else False for x in data]
    grid = [data]
    for _ in range(size - 1):
        previous = grid[-1]
        new_row = []
        for i in range(len(previous)):
            a = False if i == 0 else previous[i - 1]
            b = previous[i]
            c = False if i == len(previous) - 1 else previous[i + 1]
            new_row.append(is_a_trap(a, b, c))
        grid.append(new_row)

    return len(grid) * len(grid[0]) - sum(sum(row) for row in grid)


if __name__ == '__main__':
    data = load_data()
    print(like_rogue(data))
    print(like_rogue(data, 400000))
