import os
import re


class Game:
    def __init__(self, row):
        self.idx = int(re.search(r'Game (\d+)', row).group(1))
        self.red_cubes = list(map(int, re.findall(r'(\d+) red', row)))
        self.green_cubes = list(map(int, re.findall(r'(\d+) green', row)))
        self.blue_cubes = list(map(int, re.findall(r'(\d+) blue', row)))

    def is_avaibale(self, red, green, blue):
        return (
            all(x <= red for x in self.red_cubes)
            and
            all(x <= green for x in self.green_cubes)
            and
            all(x <= blue for x in self.blue_cubes)
        )

    def min_condition(self):
        return (
            max(self.red_cubes)
            *
            max(self.green_cubes)
            *
            max(self.blue_cubes)
        )


def load_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, 'input.txt')) as f:
        return [x.rstrip('\n') for x in f.readlines()]


def cube_conundrum(data):
    result_1 = 0
    result_2 = 0
    for row in data:
        game = Game(row)
        if game.is_avaibale(12, 13, 14):
            result_1 += game.idx
        result_2 += game.min_condition()
    return result_1, result_2


if __name__ == '__main__':
    data = load_data()

    print(cube_conundrum(data))
