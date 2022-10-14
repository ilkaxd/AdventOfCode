from collections import Counter


def load_data():
    with open(r'2019\H\input.txt') as f:
        return f.readline().strip('\n')


def split_by_layers(data, wide, tall):
    '''
    Делим строку на подстроки указанного размера
    ищем строку, в которой наименьшее количество цифр 0
    '''
    sequences_freq = []
    width = wide * tall
    for i in range(0, len(data) - 1, width):
        sequence = data[i: i + width]
        cntr = Counter(sequence)
        cntr.setdefault('0', width)
        sequences_freq.append(cntr)
    result = min(sequences_freq, key=lambda x: x['0'])
    return result['1'] * result['2']


def print_password(data, wide, tall):
    '''
    Печатаем пароль
    подстроки образуют слои
    ищем первый слой в котором по указанному
    пикселю указана цифра 0 (пропуск) или 1 (*)
    '''
    sequences = []
    width = wide * tall
    for i in range(0, len(data) - 1, width):
        sequence = data[i: i + width]
        sequences.append(sequence)
    image = ''
    for y in range(tall):
        for x in range(wide):
            for sequence in sequences:
                idx = y * wide + x
                elem = sequence[idx]
                if elem == '0':
                    image += ' '
                    break
                elif elem == '1':
                    image += '*'
                    break
                else:
                    continue
        image += '\n'
    print(image)


if __name__ == '__main__':
    data = load_data()
    print(split_by_layers(data, 25, 6))
    print_password(data, 25, 6)
