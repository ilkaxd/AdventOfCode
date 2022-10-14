import re
from collections import defaultdict, Counter


def load_data():
    with open(r'2018\C_03\input.txt') as f:
        return [x for x in f.read().split('\n') if x != '']


def find_overlap(data):
    """
    Имеется поле размера 1000х1000
    Нужно найти количество ячеек, которые
    имеют минимум одно пересечение
    """
    n = 1000
    fabric = dict(
        ((x, y), 0)
        for x in range(n)
        for y in range(n)
    )
    for row in data:
        regex = re.compile(r'(\d+,\d+): (\d+x\d+)')
        mo = regex.search(row)
        X, Y = map(int, mo.group(1).split(','))
        width, height = map(int, mo.group(2).split('x'))
        for row in range(Y, Y + height):
            for column in range(X, X + width):
                fabric[(row, column)] += 1

    result = 0
    for value in fabric.values():
        if value > 1:
            result += 1
    return result


def id_without_overlap(data):
    """
    Ищем строку, которая не перекрывалась ни разу
    """
    n = 1000
    fabric = dict(
        ((x, y), [0, []])
        for x in range(n)
        for y in range(n)
    )
    elves = defaultdict(int)
    for row in data:
        regex = re.compile(r'#(\d+) @ (\d+,\d+): (\d+x\d+)')
        mo = regex.search(row)
        _id = int(mo.group(1))
        X, Y = map(int, mo.group(2).split(','))
        width, height = map(int, mo.group(3).split('x'))
        for row in range(Y, Y + height):
            for column in range(X, X + width):
                fabric[(row, column)][0] += 1
                fabric[(row, column)][1].append(_id)
                elves[_id] += 1

    targets = Counter(
        [
            value[1][0]
            for value in fabric.values()
            if value[0] == 1
        ]
    )
    for key, value in targets.items():
        if value == elves[key]:
            return key


if __name__ == '__main__':
    data = load_data()
    print(find_overlap(data))
    print(id_without_overlap(data))
