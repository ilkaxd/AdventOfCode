from copy import copy
import sys
sys.setrecursionlimit(100000)


def load_data():
    with open((r'2021\O_15\input.txt')) as f:
        return [list(map(int, list(x.rstrip('\n')))) for x in f.readlines()]


def DFS(
    grid,
    x, y, target_x, target_y,
    visited, current_sum=0, result=float('+inf')
):
    if current_sum > result:
        return result

    if target_x == x and target_y == y:
        return current_sum

    for x_delta, y_delta in (
        (1, 0),   # вправо
        (0, 1),   # вниз
        (-1, 0),  # влево
        (0, -1),  # вверх
    ):
        new_x = x + x_delta
        new_y = y + y_delta
        if (
            (0 <= new_x <= target_x) and
            (0 <= new_y <= target_y) and
            ((new_x, new_y) not in visited)
        ):
            new_visited = copy(visited)
            new_visited.append((new_x, new_y))
            result = DFS(
                grid,
                new_x, new_y,
                target_x, target_y,
                new_visited, current_sum + grid[new_y][new_x],
                result
            )
    return result


def Chiton(data):
    results = DFS(data, 0, 0, len(data[0]) - 1, len(data) - 1, [(0, 0)])
    return results


if __name__ == '__main__':
    data = load_data()
    data = [
        [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
        [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
        [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
        [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
        [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
        [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
        [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
        [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
        [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
        [2, 3, 1, 1, 9, 4, 4, 5, 8, 1],
    ]
    print(Chiton(data))
