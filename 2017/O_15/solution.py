def load_data():
    with open(r'2017\O_15\input.txt') as f:
        return [int(x.split()[-1]) for x in f.readlines()]


def dueling_generators(a, b, size=40_000_000):
    '''
    Ищем числа у которых 16 наименьших бит совпадают
    итерация по числам идёт по определённому правилу
    '''
    factor_a = 16807
    factor_b = 48271
    denominator = 2147483647
    result = 0
    for _ in range(size):
        a = (a * factor_a) % denominator
        b = (b * factor_b) % denominator
        hex_a = '{0:b}'.format(a).rjust(16, '0')[-16:]
        hex_b = '{0:b}'.format(b).rjust(16, '0')[-16:]
        if hex_a == hex_b:
            result += 1
    return result


def dueling_generators_2(a, b, size=5_000_000):
    factor_a = 16807
    denominator_a = 4
    factor_b = 48271
    denominator_b = 8
    denominator = 2147483647
    result = 0
    for _ in range(size):
        a = (a * factor_a) % denominator
        while a % denominator_a != 0:
            a = (a * factor_a) % denominator
        b = (b * factor_b) % denominator
        while b % denominator_b != 0:
            b = (b * factor_b) % denominator

        hex_a = '{0:b}'.format(a).rjust(16, '0')[-16:]
        hex_b = '{0:b}'.format(b).rjust(16, '0')[-16:]
        if hex_a == hex_b:
            result += 1
    return result


if __name__ == '__main__':
    data = load_data()
    print(dueling_generators(*data))
    print(dueling_generators_2(*data))
