import copy, re


def load_data():
    with open(r'2016\H_08\input.txt') as f:
        return f.readlines()


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = [
            [
                0 for _ in range(self.width)
            ] for _ in range(self.height)
        ]

    def __str__(self):
        return '\n'.join(
           ' '.join(
            '.'
            if self.array[row][column] == 0 else '#'
            for column in range(self.width)
        )
        for row in range(self.height)
    )

    def create(self, width, height):
        for row in range(height):
            for column in range(width):
                self.array[row][column] = 1

    def rotate_column(self, column, shift):
        for _ in range(shift):
            self.rotate_column_by_one(column)

    def rotate_column_by_one(self, column):
        new_array = copy.deepcopy(self.array)
        for row in range(self.height):
            new_array[row][column] = self.array[row - 1][column]
        self.array = new_array

    def rotate_row(self, row, shift):
        for _ in range(shift):
            self.rotate_row_by_one(row)

    def rotate_row_by_one(self, row):
        new_array = copy.deepcopy(self.array)
        for column in range(self.width):
            new_array[row][column] = self.array[row][(column - 1)]
        self.array = new_array

    def parse_string(self, command):
        regex_1 = re.compile(r'rect (\d+)x(\d+)')
        regex_2 = re.compile(r'rotate row y=(\d+) by (\d+)')
        regex_3 = re.compile(r'rotate column x=(\d+) by (\d+)')

        if regex_1.search(command):
            width = int(regex_1.search(command).group(1))
            height = int(regex_1.search(command).group(2))
            self.create(width, height)
        elif regex_2.search(command):
            x = int(regex_2.search(command).group(1))
            shift = int(regex_2.search(command).group(2))
            self.rotate_row(x, shift)
        elif regex_3.search(command):
            y = int(regex_3.search(command).group(1))
            shift = int(regex_3.search(command).group(2))
            self.rotate_column(y, shift)
        else:
            print('Нераспознная команда')

    def count_ones(self):
        return sum(sum(column) for column in self.array)


def use_command(data):
    """
    Имеется дисплей размера 50x6
    На вход приходят 3 типа команд:
        -   rect AxB - включает все пиксели в квадрате
        AxB
        - rotate row y=A by B - смещает все пиксели в строке A
        на B вправо
        - rotate column x=A by B - смещает все пиксели в столбце A
        на B вниз
    дисплей цикличный, то что ушло направо, появляется слева
    а то что ушло вниз, сверху

    После выполнения действия выводим на экран вывод программы
    """
    screen = Screen(50, 6)
    for row in data:
        screen.parse_string(row.strip('\n'))
    print(screen)
    return screen.count_ones()


if __name__ == '__main__':
    data = load_data()
    print(use_command(data))
