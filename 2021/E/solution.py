from collections import defaultdict


def load_data():
    with open(r'2021\E\input.txt') as f:
        return [x for x in f.read().split('\n') if x != '']


def hydrothermal_venture(data):
    '''
    Имеются прямоугольные линии в
    формате x1,y1 -> x2,y2
    Они могут быть только вертикальными
    или горизонтальными
    Нужно найти количество пересечений линий
    '''
    grid = defaultdict(int)
    for row in data:
        start, end = row.split(' -> ')
        x_1, y_1 = map(int, start.split(','))
        x_2, y_2 = map(int, end.split(','))
        # Вертикальная линия
        if x_1 == x_2:
            start, end = min(y_1, y_2), max(y_1, y_2)
            for y in range(start, end + 1):
                grid[(x_1, y)] += 1
        # Горизонтальная линия
        elif y_1 == y_2:
            start, end = min(x_1, x_2), max(x_1, x_2)
            for x in range(start, end + 1):
                grid[(x, y_1)] += 1
    return sum(1 for value in grid.values() if value > 1)


def hydrothermal_venture_2(data):
    '''
    Учитываем также диагонали
    '''
    grid = defaultdict(int)
    for row in data:
        start, end = row.split(' -> ')
        x_1, y_1 = map(int, start.split(','))
        x_2, y_2 = map(int, end.split(','))
        # Вертикальная линия
        if x_1 == x_2:
            start, end = min(y_1, y_2), max(y_1, y_2)
            for y in range(start, end + 1):
                grid[(x_1, y)] += 1
        # Горизонтальная линия
        elif y_1 == y_2:
            start, end = min(x_1, x_2), max(x_1, x_2)
            for x in range(start, end + 1):
                grid[(x, y_1)] += 1
        # Диагональная линия
        else:
            # Положительный тангенс
            if (
                (y_2 > y_1 and x_2 > x_1)
                or
                (y_1 > y_2 and x_1 > x_2)
            ):
                x_1, x_2 = min(x_1, x_2), max(x_1, x_2)
                y_1, y_2 = min(y_1, y_2), max(y_1, y_2)
                for x, y in zip(range(x_1, x_2 + 1), range(y_1, y_2 + 1)):
                    grid[(x, y)] += 1
            # Отрицательный тангенс
            else:
                x_1, x_2 = min(x_1, x_2), max(x_1, x_2)
                y_1, y_2 = min(y_1, y_2), max(y_1, y_2)
                for x, y in zip(range(x_1, x_2 + 1), range(y_2, y_1 - 1, -1)):
                    grid[(x, y)] += 1

    return sum(1 for value in grid.values() if value > 1)


if __name__ == '__main__':
    data = load_data()
    print(hydrothermal_venture(data))
    print(hydrothermal_venture_2(data))
