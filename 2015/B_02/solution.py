def load_data():
    with open(r'2015\B_02\input.txt') as f:
        return f.read()


def find_square(dimensions):
    """
    Ищем площадь параллелограмма и
    добавляем площадь наименьшей стороны
    """
    l, w, h = map(int, dimensions.split('x'))
    first = l * w
    second = w * h
    third = h * l
    return (
        2 * first +
        2 * second +
        2 * third +
        min([first, second, third])
    )


def find_ribbon_length(dimensions):
    """
    Ищем минимальный периметр и добавляем объём
    """
    l, w, h = map(int, dimensions.split('x'))
    first = 2 * l + 2 * w
    second = 2 * w + 2 * h
    third = 2 * h + 2 * l
    return min([first, second, third]) + volume(l, w, h)


def volume(x, y, z):
    return x * y * z


def find_squares(sequence):
    return sum(
        find_square(x)
        for x in sequence
        if x != ''
    )


def find_lengths(sequence):
    return sum(
        find_ribbon_length(x)
        for x in sequence
        if x != ''
    )


if __name__ == '__main__':
    data = load_data().split('\n')
    print(find_squares(data))
    print(find_lengths(data))
