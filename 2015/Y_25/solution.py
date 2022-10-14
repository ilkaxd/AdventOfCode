import re


def load_data():
    with open(r'2015\Y\input.txt') as f:
        regex = re.compile(r'\d+')
        return regex.findall(f.read())


def build_graph(target_row, target_column):
    max_row, min_column = 1, 1
    value = 20151125
    while True:
        max_row += 1
        for delta in range(0, max_row):
            row = max_row - delta
            column = min_column + delta
            value = (value * 252533) % 33554393
            if row == target_row and column == target_column:
                return value


if __name__ == '__main__':
    row, column = load_data()
    print(build_graph(int(row), int(column)))
