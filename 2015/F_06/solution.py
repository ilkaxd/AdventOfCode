import re

numbers = r'(\d*,\d*)'


def load_data():
    with open(r'2015\F_06\input.txt') as f:
        return f.read()


def First(instructions):
    """
    Каждая строка соответствует прямоугольнику, у которого указана
    левая верхняя и правая нижняя вершины. Инструкции выполняются для
    всех элементов из указанного интервала
    """
    array = [[False for _ in range(1_000)] for _ in range(1_000)]
    for instruction in instructions:
        left, right = re.findall(numbers, instruction)
        left_x, left_y = map(int, left.split(','))
        right_x, right_y = map(int, right.split(','))
        for i in range(left_x, right_x + 1):
            for j in range(left_y, right_y + 1):
                if 'turn on' in instruction:
                    array[i][j] = True
                if 'turn off' in instruction:
                    array[i][j] = False
                if 'toggle' in instruction:
                    array[i][j] = not array[i][j]
    return sum(sum(row) for row in array)


def Second(instructions):
    """
    Изменили правила:
        - turn on - увеличивает яркость ячейки на 1
        - turn off - уменьшает яркость ячейки на 1
        - toggle - увеличивает яркость ячейки на 2
    """
    array = [[0 for _ in range(1_000)] for _ in range(1_000)]
    for instruction in instructions:
        left, right = re.findall(numbers, instruction)
        left_x, left_y = map(int, left.split(','))
        right_x, right_y = map(int, right.split(','))
        for i in range(left_x, right_x + 1):
            for j in range(left_y, right_y + 1):
                if 'turn on' in instruction:
                    array[i][j] += 1
                if 'turn off' in instruction:
                    array[i][j] = max(0, array[i][j] - 1)
                if 'toggle' in instruction:
                    array[i][j] += 2
    return sum(sum(row) for row in array)


if __name__ == '__main__':
    data = [x for x in load_data().split('\n') if x != '']
    print(First(data))
    print(Second(data))
