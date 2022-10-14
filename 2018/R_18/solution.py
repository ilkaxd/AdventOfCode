from collections import Counter


def load_data():
    with open(r'2018\R_18\input.txt') as f:
        return [list(x.strip('\n')) for x in f.readlines()]


def update_cell(x, y, data, new_data, max_x, max_y):
    result = []
    for new_x, new_y in (
        (x - 1, y),
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
        (x, y + 1),
        (x - 1, y + 1)
    ):
        if (0 <= new_x < max_x and 0 <= new_y < max_y):
            result.append(data[new_y][new_x])

    result = Counter(result)
    current_cell = data[y][x]
    if current_cell == '.':
        if result['|'] >= 3:
            new_data[y][x] = '|'
    elif current_cell == '|':
        if result['#'] >= 3:
            new_data[y][x] = '#'
    elif current_cell == '#':
        if not (result['#'] >= 1 and result['|'] >= 1):
            new_data[y][x] = '.'


def prid_grid(data):
    for row in data:
        print(''.join(row))
    print()


def clone(data):
    return [[x for x in row] for row in data]


def settlers_of_north_pole(data, minutes=10):
    max_y = len(data)
    max_x = len(data[0])
    history = []
    start_idx = None
    periodicity = None
    i = 0
    while (
        i < minutes
        and
        periodicity is None
    ):
        new_data = clone(data)
        for y in range(max_y):
            for x in range(max_x):
                update_cell(x, y, data, new_data, max_x, max_y)
        if new_data in history:
            if start_idx is None:
                start_idx = history.index(new_data)
                periodicity = len(history) - start_idx
        history.append(new_data)
        data = new_data
        i += 1

    if start_idx is not None:
        remaining = minutes - 1 - start_idx
        data = history[start_idx + remaining % periodicity]

    flat_data = [item for sublist in data for item in sublist]
    counter = Counter(flat_data)
    return counter['|'] * counter['#']


if __name__ == '__main__':
    data = load_data()
    print(settlers_of_north_pole(data))
    print(settlers_of_north_pole(data, 1_000_000_000))
