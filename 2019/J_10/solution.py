from collections import defaultdict


def load_data():
    with open(r'2019\J_10\input.txt') as f:
        return [list(x.strip('\n')) for x in f.readlines()]


def linear_model(x1, y1, x2, y2):
    '''
    (x - x1)/(x1 - x2) = (y - y1)/(y1 - y2)

    | y1 = kx1 + b
    | y2 = kx2 + b
    b = y2 — kx2
    y1 = kx1 + y2 — kx2
    k = (y1 — y2) / (x1 — x2)
    '''
    k = (y1 - y2) / (x1 - x2) if x1 != x2 else 0
    b = y2 - k * x2
    return k, b


def monitoring_station(grid):
    results = defaultdict(list)
    for Y in range(len(grid)):
        for X in range(len(grid[0])):
            station = grid[Y][X]
            if station == '#':
                for y in range(len(grid)):
                    for x in range(len(grid)):
                        if X == x and Y == y:
                            continue
                        asteroid = grid[y][x]
                        if asteroid != '#':
                            continue
                        results[(X, Y)].append(linear_model(x, y, X, Y))
    for key in results.keys():
        results[key] = len(set(results[key]))
    return results


if __name__ == '__main__':
    data = load_data()
    data = [
        ['.', '#', '.', '.', '#'],
        ['.', '.', '.', '.', '.'],
        ['#', '#', '#', '#', '#'],
        ['.', '.', '.', '.', '#'],
        ['.', '.', '.', '#', '#'],
    ]
    print(monitoring_station(data))
