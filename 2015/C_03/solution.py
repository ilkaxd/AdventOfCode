from collections import namedtuple


class Position(namedtuple('Point', ['x', 'y'])):
    pass


def load_data():
    with open(r'2015\C_03\input.txt') as f:
        return f.read()


def find_unique_houses(actions):
    """
    Считаем количество уникальных значений в 2D пространстве
    при перемещении:
        -   влево (<)
        -   вправо (>)
        -   вверх (^)
        -   вниз (v)
    """
    current = Position(0, 0)
    visited = [current]
    for action in actions:
        new_position = None
        if action == '<':
            new_position = current._replace(x=current.x - 1)
        if action == '>':
            new_position = current._replace(x=current.x + 1)
        if action == '^':
            new_position = current._replace(y=current.y + 1)
        if action == 'v':
            new_position = current._replace(y=current.y - 1)
        visited.append(new_position)
        current = new_position
    return len(set(visited))


def find_unique_houses_2(actions):
    """
    Появилась дополнительная отслеживаемая точка.
    Инструкции для каждой точки чередуются.
    """
    Santa = Position(0, 0)
    RoboSanta = Position(0, 0)
    current = Santa
    visited = [current]
    for action in actions:
        new_position = None
        if action == '<':
            new_position = current._replace(x=current.x - 1)
        if action == '>':
            new_position = current._replace(x=current.x + 1)
        if action == '^':
            new_position = current._replace(y=current.y + 1)
        if action == 'v':
            new_position = current._replace(y=current.y - 1)
        visited.append(new_position)
        if current == Santa:
            current = RoboSanta
            Santa = new_position
        else:
            current = Santa
            RoboSanta = new_position
    return len(set(visited))


if __name__ == '__main__':
    data = load_data()
    print(find_unique_houses(data))
    print(find_unique_houses_2(data))
