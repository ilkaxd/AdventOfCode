def load_data():
    with open(r'2016\X_24\input.txt') as f:
        return [list(x.rstrip('\n')) for x in f.readlines()]


def DFS(
    x, y,
    grid, points,
    visited = [],
    step=0, min_step=100_000
):
    if all(points.values()):
        return min(step, min_step)
    if step > 100 or step > min_step:
        return min_step
    for x_delta, y_delta in (
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, 1)
    ):
        x_new, y_new = x + x_delta, y + y_delta
        cell = grid[y_new][x_new]
        if cell == '#' or (x_new, y_new) in visited[:-5]:
            continue

        new_visited = [value for value in visited]
        new_visited.append((x_new, y_new))
        new_points = dict(
            (key, value)
            for key, value in points.items()
        )

        if cell != '.':
            new_points[cell] = True
        min_step = DFS(
            x_new, y_new,
            grid,
            new_points, new_visited,
            step + 1, min_step
        )
    return min_step


def duct_spelunking(grid):
    points = {}
    x_init, y_init = None, None
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            cell = grid[y][x]
            if cell not in '#.':
                points[cell] = False
                if cell == '0':
                    x_init, y_init = x, y

    points['0'] = True
    return DFS(x_init, y_init, grid, points)


if __name__ == '__main__':
    data = load_data()
    data = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '0', '.', '1', '.', '.', '.', '.', '.', '2', '#'],
        ['#', '.', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
        ['#', '4', '.', '.', '.', '.', '.', '.', '.', '3', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    print(duct_spelunking(data))
