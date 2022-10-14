def load_data():
    with open(r'2019\P_16\input.txt') as f:
        return f.readline().rstrip('\n')


def calculate_value(data, base_pattern, i):
    pattern = []
    size = len(data)
    for x in base_pattern:
        pattern += [x] * i
    repeated = size // len(pattern) + 1
    pattern = pattern * repeated
    result = 0
    pattern = pattern[1:size + 1]
    for value, value_pattern in zip(data, pattern):
        result += value * value_pattern
    return abs(result) % 10


def FFT(data, phase_count=100):
    base_pattern = [0, 1, 0, -1]
    data = list(map(int, data))
    size = len(data)

    for _ in range(phase_count):
        new_data = [x for x in data]
        for i in range(size):
            new_data[i] = calculate_value(data, base_pattern, i + 1)
        data = new_data
    return ''.join(str(x) for x in data)


def FFT_with_shift(data, phase_count=100):
    shift = int(data[0]) + int(data[1:3]) + int(data[3:7])
    result = FFT(data, phase_count)
    return result[shift: shift+8]


if __name__ == '__main__':
    data = load_data()
    # assert FFT('12345678', 4) == '01029498'
    # assert FFT('80871224585914546619083218645595')[:8] == '24176176'
    # assert FFT('19617804207202209144916044189917')[:8] == '73745418'
    # assert FFT('69317163492948606335995924319873')[:8] == '52432133'
    # print(FFT(data *)[:8])
    print(FFT_with_shift(data * 10_000))
