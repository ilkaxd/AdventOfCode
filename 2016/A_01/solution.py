def load_data():
    with open(r'2016\A_01\input.txt') as f:
        return f.read().strip('\n').split(', ')


def changeDirection(direction_x, direction_y, action):
    if action.startswith('L'):
        if direction_y == 1:
            direction_y = 0
            direction_x = -1
        elif direction_y == -1:
            direction_y = 0
            direction_x = 1
        elif direction_x == 1:
            direction_x = 0
            direction_y = 1
        elif direction_x == -1:
            direction_x = 0
            direction_y = -1
    elif action.startswith('R'):
        if direction_y == 1:
            direction_y = 0
            direction_x = 1
        elif direction_y == -1:
            direction_y = 0
            direction_x = -1
        elif direction_x == 1:
            direction_x = 0
            direction_y = -1
        elif direction_x == -1:
            direction_x = 0
            direction_y = 1
    return direction_x, direction_y


def findMinDistance(actions):
    """
    Дана последовательность действий.
    Изначально мы смотрим на север
    L и R обозначают поворот на 90 градусов
    цифра означает движение вперёд
    """
    x = 0
    y = 0
    direction_x = 0
    direction_y = 1
    for action in actions:
        direction_x, direction_y = changeDirection(
            direction_x,
            direction_y,
            action
        )
        value = int(action[1:])
        x += direction_x * value
        y += direction_y * value
    return abs(x) + abs(y)


def findFirstSamePoints(actions):
    """
    Ищем первую точку, которую мы посетили дважды
    """
    visited = []
    x = 0
    y = 0
    previous_x = 0
    previous_y = 0
    direction_x = 0
    direction_y = 1
    for i, action in enumerate(actions):
        direction_x, direction_y = changeDirection(
            direction_x,
            direction_y,
            action
        )
        value = int(action[1:])
        x += direction_x * value
        y += direction_y * value

        if direction_x != 0:
            for x_i in range(previous_x, x, direction_x):
                if (x_i, y) in visited:
                    return abs(x_i) + abs(y)
                visited.append((x_i, y))
        else:
            for y_i in range(previous_y, y, direction_y):
                if (x, y_i) in visited:
                    return abs(x) + abs(y_i)
                visited.append((x, y_i))
        previous_x = x
        previous_y = y


if __name__ == '__main__':
    data = load_data()
    print(findMinDistance(data))
    print(findFirstSamePoints(data))
