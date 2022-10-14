import copy

class Octopus:
    def __init__(self, state):
        self.state = state
        self.shine = False

    def start_shine(self):
        if self.state > 9 and not self.shine:
            self.shine = True
            return True
        return False


def load_data():
    with open((r'2021\K\input.txt')) as f:
        return [list(map(int, r.rstrip('\n'))) for r in f.readlines()]


def DumboOctopus(grid, n=90):
    result = 0
    height = len(grid)
    width = len(grid[0])
    for _ in range(n):
        for row in range(height):
            for column in range(width):
                grid[row][column] += 1

        repeat = True
        while repeat:
            repeat = False
            new_grid = copy.deepcopy(grid)
            for row in range(height):
                for column in range(width):
                    if grid[row][column] == 10:
                        repeat = True
                        # слева
                        if column > 0:
                            new_grid[row][column - 1] += 1
                        # слева сверху
                        if column > 0 and row > 0:
                            new_grid[row - 1][column - 1] += 1
                        # слева снизу
                        if column > 0 and row < height - 1:
                            new_grid[row + 1][column - 1] += 1
                        # справа
                        if column < width - 1:
                            new_grid[row][column + 1] += 1
                        # справа сверху
                        if column < width - 1 and row > 0:
                            new_grid[row - 1][column + 1] += 1
                        # справа снизу
                        if column < width - 1 and row < height - 1:
                            new_grid[row + 1][column + 1] += 1
                        # сверху
                        if row > 0:
                            new_grid[row - 1][column] += 1
                        # снизу
                        if row < height - 1:
                            new_grid[row + 1][column] += 1
                        # центр
                        new_grid[row][column] += 1
            grid = new_grid
        # Считаем количество вспышек
        for row in range(height):
            for column in range(width):
                if grid[row][column] > 10:
                    result += 1
                    grid[row][column] = 0
        continue
    return result


if __name__ == '__main__':
    data = load_data()
    data = [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]
    print(DumboOctopus(data, 100))
