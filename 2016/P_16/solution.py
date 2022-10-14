def load_data():
    with open(r'2016\P_16\input.txt') as f:
        return list(map(int, f.readline()))


def dragon_curve(data):
    a = data
    b = [x for x in a]
    b = b[::-1]
    b = [int(not x) for x in b]
    return a + [0] + b


def checksum(data):
    pairs = []
    for i in range(0, len(data), 2):
        pairs.append((data[i], data[i + 1]))
    result = [1 if x == y else 0 for x, y in pairs]
    if len(result) % 2 == 0:
        return checksum(result)
    return result


def dragon_checksum(data, length):
    # Формируем последовательность
    while len(data) < length:
        data = dragon_curve(data)
    data = data[:length]
    # Вычисляем checksum
    return ''.join(str(x) for x in checksum(data))


if __name__ == '__main__':
    data = load_data()
    print(dragon_checksum(data, 272))
    print(dragon_checksum(data, 35651584))
