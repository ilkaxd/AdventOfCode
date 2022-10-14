from collections import defaultdict
from itertools import product


def load_data():
    with open((r'2021\T_20\input.txt')) as f:
        return f.read()


def print_grid(grid):
    for y in range(-5, 10):
        for x in range(-5, 10):
            print('#' if grid[(x, y)] else '.', end='')
        print()
    print()


def get_state(x, y, grid, algorithm):
    number = ''
    for (x_delta, y_delta) in product((-1, 0, 1), repeat=2):
        number += '1' if grid[(x + x_delta, y + y_delta)] else '0'
    shift = int(number, 2)
    if algorithm[shift] == '#':
        return True
    return False


def trench_map(algorithm, image):
    grid = defaultdict(bool)

    for y in range(len(image)):
        for x in range(len(image[0])):
            cell = image[y][x]
            if cell == '#':
                grid[(x, y)] = True
            else:
                grid[(x, y)] = False
    for _ in range(2):
        new_grid = grid.copy()
        min_x, min_y = min(grid.keys())
        max_x, max_y = max(grid.keys())
        for x in range(min_x - 100, max_x + 100):
            for y in range(min_y - 100, max_y + 100):
                new_grid[(x, y)] = get_state(x, y, grid, algorithm)
        grid = new_grid
    return sum(grid.values())


if __name__ == '__main__':
    data = load_data()
    algorithm, image = data.split('\n\n')
    algorithm = algorithm.rstrip('\n')
    image = [
        list(row.rstrip('\n'))
        for row in image.rstrip('\n').split('\n')
    ]
    algorithm = '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#'
    image = [
        ['#', '.', '.', '#', '.'],
        ['#', '.', '.', '.', '.'],
        ['#', '#', '.', '.', '#'],
        ['.', '.', '#', '.', '.'],
        ['.', '.', '#', '#', '#'],
    ]
    # print(image)
    print(trench_map(algorithm, image))
