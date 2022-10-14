def load_data():
    with open(r'2015\K_11\input.txt') as f:
        return f.readline().strip('\n')


def is_valid_password(password):
    """
    Пароль верный, если:
        - есть возрастающая последовательность
        минимум из 3 букв: abc, bcd но не abd
        - нет символов i, o, l
        - если минимум 2 различных, непересекающихся
        пары букв: aa, bb
    """
    is_valid = False
    for i in range(1, len(password) - 1):
        first = password[i - 1]
        second = password[i]
        third = password[i + 1]
        value_first = ord(first)
        value_second = ord(second)
        value_third = ord(third)
        if (value_first + 2) == (value_second + 1) == value_third:
            is_valid = True
            break

    if not is_valid:
        return False

    is_valid = all(ch not in ['i', 'o', 'l'] for ch in password)

    if not is_valid:
        return False

    count = 0
    not_overlapping = True
    for i in range(len(password) - 1):
        first = password[i]
        second = password[i + 1]
        if first == second and not_overlapping:
            count += 1
            not_overlapping = False
            continue
        not_overlapping = True

    is_valid = count >= 2
    return is_valid


def increace_password(password):
    """
    Новый пароль формируется путём увеличения
    крайнего правого значения на 1:
    xx, xy, xz, ya, yb
    """
    low_limit = ord('a')
    up_limit = ord('z')
    result = ''
    inc = 1
    for ch in password[::-1]:
        value = ord(ch)
        value += inc
        if value > up_limit:
            value = low_limit
        else:
            inc = 0
        result += chr(value)
    return result[::-1]


def find_right_password(data):
    while not is_valid_password(data):
        data = increace_password(data)
    return data


def find_new_password(password):
    password = increace_password(password)
    new_password = find_right_password(password)
    return new_password


if __name__ == '__main__':
    data = load_data()
    new_password = find_new_password(data)
    print(new_password)
    new_password_2 = find_new_password(new_password)
    print(new_password_2)
