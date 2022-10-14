def load_data():
    with open(r'2016\M_13\input.txt') as f:
        return int(f.read())


def is_open_space(x, y, favorite_number):
    """
    Проверка является ли ячейка стеной
    """
    if x < 0 or y < 0:
        return False
    result = x*x + 3*x  + 2*x*y + y + y*y
    result += favorite_number
    result = bin(result)
    result = [1 for x in str(result) if x == '1']
    result = sum(result)
    return result % 2 == 0


def watch_area(x, y, area, favorite_number, point):
    for row in range(0, 50):
        for column in range(0, 50):
            if point[1] == row and point[0] == column:
                print('O', end='')
                continue

            if row == y and column == x:
                print('+', end='')
                continue
            condition = is_open_space(column, row, favorite_number)
            if condition:
                print('.', end='')
            else:
                print('#', end='')
        print()


def Maze(
    x, y,
    favorite_number, visited,
    steps,
    target_x, target_y,
    move='', current_min=float('inf')
):
    """
    Считаем минимальное количество шагов, которые нужно пройти
    по лабиринту чтобы из точки A попасть в точку B
    """
    if steps > current_min:
        return current_min
    new_visited = visited.copy()
    new_visited.append((x, y))
    move += f'->({x}{y})'
    if x == target_x and y == target_y:
        return min(current_min, steps)
    up = (x, y - 1)
    down = (x, y + 1)
    left = (x - 1, y)
    right = (x + 1, y)
    for new_x, new_y in [
        left, right, up, down,
    ]:
        if (
            is_open_space(new_x, new_y, favorite_number) and
            (new_x, new_y) not in visited
        ):

            current_min = Maze(
                new_x, new_y, favorite_number,
                new_visited, steps + 1,
                target_x, target_y,
                move, current_min
            )
    return current_min


def Maze_2(
    x, y,
    favorite_number, visited,
    steps, max_steps,
    all_visited
):
    """
    Считаем количество уникальных мест,
    которые мы можем посетить за max_steps шагов
    """
    if steps >= max_steps:
        return

    all_visited.append((x, y))
    new_visited = visited.copy()
    new_visited.append((x, y))

    up = (x, y - 1)
    down = (x, y + 1)
    left = (x - 1, y)
    right = (x + 1, y)
    for new_x, new_y in [
        left, right, up, down,
    ]:
        if (
            is_open_space(new_x, new_y, favorite_number) and
            (new_x, new_y) not in visited
        ):

            Maze_2(
                new_x, new_y, favorite_number,
                new_visited,
                steps + 1, max_steps,
                all_visited
            )
    return len(set(all_visited))


if __name__ == '__main__':
    data = load_data()
    print(Maze(
        x=1, y=1,
        favorite_number=data,
        visited=[], steps=0,
        target_x=31, target_y=39,
    ))

    print(Maze_2(
        x=1, y=1,
        favorite_number=data,
        visited=[],
        steps=0, max_steps=50 + 1,
        all_visited=[]
    ))
