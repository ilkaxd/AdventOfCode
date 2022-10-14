def load_data():
    with open(r'2017\S_19\input.txt') as f:
        return [list(x.strip('\n')) for x in f.readlines()]


def step(x, y, direction, data):
    actions = {
        'U': (0, -1),
        'L': (-1, 0),
        'D': (0, 1),
        'R': (1, 0)
    }
    x_delta, y_delta = actions[direction]
    return x + x_delta, y + y_delta


def change_direction(x, y, x_previous, y_previous, data):
    for new_direction in ['U', 'L', 'D', 'R']:
        new_x, new_y = step(x, y, new_direction, data)
        if new_x == x_previous and new_y == y_previous:
            continue
        ch = data[new_y][new_x]
        if ch != '|' and ch != ' ' and new_direction in ['L', 'R']:
            return new_direction
        elif ch != '-' and ch != ' ' and new_direction in ('U', 'D'):
            return new_direction
    return None


def series_of_tube(data):
    result = ''
    y = 0
    x = data[y].index('|')
    direction = 'D'
    x_history = None
    y_history = None
    steps = 0
    while data[y][x] != ' ':
        steps += 1
        position = data[y][x]
        if position == '+':
            direction = change_direction(x, y, x_history, y_history, data)
        else:
            if position not in ('|', '-', '+'):
                result += position
        x_history = x
        y_history = y
        x, y = step(x, y, direction, data)
    return result, steps


if __name__ == '__main__':
    data = load_data()
    print(series_of_tube(data))
