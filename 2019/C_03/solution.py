from collections import defaultdict


def load_data():
    with open(r'2019\C_03\input.txt') as f:
        return [
            [(g[0], int(g[1:])) for g in x.split(',')]
            for x in f.read().split('\n')
            if x != ''
        ]


def crossed_wires(data):
    """
    Ищем ближайшую к началу координат точку пересечения
    2 линий (в рамках одной линии могут появляться точки пересечения,
    но мы их не учитываем)
    Каждая линия определяется отдельной строкой
    Вычисляем манхетонское расстояние до пересечения
    """
    panel = defaultdict(dict)

    for row, row_value in zip(data, ['A', 'B']):
        X, Y, step = 0, 0, 0
        for action, value in row:
            new_X, new_Y = X, Y

            if action == 'U':
                new_Y += value
                for step_Y in range(Y + 1, new_Y + 1):
                    step += 1
                    panel[(new_X, step_Y)][row_value] = step
            elif action == 'D':
                new_Y -= value
                for step_Y in range(new_Y, Y):
                    step += 1
                    panel[(new_X, step_Y)][row_value] = step
            elif action == 'L':
                new_X -= value
                for step_X in range(new_X, X):
                    step += 1
                    panel[(step_X, new_Y)][row_value] = step
            elif action == 'R':
                new_X += value
                for step_X in range(X + 1, new_X + 1):
                    step += 1
                    panel[(step_X, new_Y)][row_value] = step
            X, Y = new_X, new_Y

    panel[(0, 0)] = {}

    intersections = []
    for key, value in panel.items():
        if len(set(value)) == 2:
            summa = abs(key[0]) + abs(key[1])
            intersections.append(summa)
    return min(intersections)


def crossed_wires_2(data):
    """
    Сумма путей до точки пересечения
    должна быть минимальна
    """
    panel = defaultdict(dict)

    for row, row_value in zip(data, ['A', 'B']):
        X, Y, step = 0, 0, 0
        for action, value in row:
            new_X, new_Y = X, Y

            if action == 'U':
                new_Y += value
                for step_Y in range(Y + 1, new_Y + 1):
                    step += 1
                    panel[(new_X, step_Y)].setdefault(row_value, step)
            elif action == 'D':
                new_Y -= value
                for step_Y in range(Y - 1, new_Y - 1, -1):
                    step += 1
                    panel[(new_X, step_Y)].setdefault(row_value, step)
            elif action == 'L':
                new_X -= value
                for step_X in range(X - 1, new_X - 1, -1):
                    step += 1
                    panel[(step_X, new_Y)].setdefault(row_value, step)
            elif action == 'R':
                new_X += value
                for step_X in range(X + 1, new_X + 1):
                    step += 1
                    panel[(step_X, new_Y)].setdefault(row_value, step)
            X, Y = new_X, new_Y

    panel[(0, 0)] = {}

    intersections = []
    for _, value in panel.items():
        if len(set(value)) == 2:
            summa = sum(value.values())
            intersections.append(summa)
    return min(intersections)


if __name__ == '__main__':
    data = load_data()
    print(crossed_wires(data))
    print(crossed_wires_2(data))
