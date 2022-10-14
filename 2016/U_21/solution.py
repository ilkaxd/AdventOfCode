import re

def load_data():
    with open(r'2016\U_21\input.txt') as f:
        return f.readlines()


def swap_position(password, x, y):
    password[x], password[y] = password[y], password[x]


def swap_letter(password, x, y):
    for i in range(len(password)):
        e = password[i]
        if e == x:
            password[i] = y
        elif e == y:
            password[i] = x


def rotate_direction_one(password, direction):
    if direction == 'left':
        return password[1:] + password[:1]
    return password[-1:] + password[:-1]


def rotate_direction(password, direction, shift, reverse):
    if reverse:
        if direction == 'left':
            direction = 'right'
        else:
            direction = 'left'
    for _ in range(shift):
        password = rotate_direction_one(password, direction)
    return password


def rotate_position(password, value, reverse):
    idx = password.index(value)

    if reverse:
        idx -= 1
        shift = 0 + 1
        if idx < 0:
            idx = len(password) + idx
        if idx >= 4:
            shift += 1
        else:
            idx -= 1
        shift += idx
    else:
        shift = idx
        if shift >= 4:
            shift += 1
        shift += 1
    return rotate_direction(password, 'right', shift, reverse)


def reverse_position(password, x, y):
    reverse_password = password[x:y + 1][::-1]
    password[x:y + 1] = reverse_password
    return password


def move_position(password, x, y, reverse):
    if reverse:
        x, y = y, x
    element = password.pop(x)
    return password[:y] + [element] + password[y:]


def scrambled_letter(password, actions, reverse=False):
    password = list(password)

    if reverse:
        actions = actions[::-1]

    swap_position_regex = re.compile(
        r'swap position (\d+) with position (\d+)'
    )

    swap_letter_regex = re.compile(
        r'swap letter (\w) with letter (\w)'
    )

    rotate_direction_regex = re.compile(
        r'rotate (left|right) (\d+) step'
    )

    rotate_position_regex = re.compile(
        r'rotate based on position of letter (\w)'
    )

    reverse_position_regex = re.compile(
        r'reverse positions (\d+) through (\d+)'
    )

    move_position_regex = re.compile(
        r'move position (\d+) to position (\d+)'
    )

    for action in actions:
        if swap_position_regex.search(action) is not None:
            values = map(int, swap_position_regex.search(action).groups(1))
            swap_position(password, *values)
        elif swap_letter_regex.search(action) is not None:
            values = swap_letter_regex.search(action).groups(1)
            swap_letter(password, *values)
        elif rotate_direction_regex.search(action) is not None:
            values = rotate_direction_regex.search(action).groups(1)
            password = rotate_direction(
                password,
                values[0], int(values[1]),
                reverse
            )
        elif rotate_position_regex.search(action) is not None:
            values = rotate_position_regex.search(action).groups(1)
            password = rotate_position(password, *values, reverse)
        elif reverse_position_regex.search(action) is not None:
            values = map(int, reverse_position_regex.search(action).groups(1))
            password = reverse_position(password, *values)
        elif move_position_regex.search(action) is not None:
            values = map(int, move_position_regex.search(action).groups(1))
            password = move_position(password, *values, reverse)
    return ''.join(password)


if __name__ == '__main__':
    data = load_data()
    password = 'abcdefgh'
    print(scrambled_letter(password, data))
    password = 'fbgdceah'
    print(scrambled_letter(password, data, True))


