def load_data():
    with open(r'2017\B\input.txt') as f:
        return [
            list(map(int, x.split('\t')))
            for x in f.read().split('\n')
            if x != ''
        ]


def corruption_checksum(data):
    """
    Вычисляем разницу между максимальным
    и минимальным элементом в каждой строке
    Полученные числа складываем
    """
    return sum([max(x) - min(x) for x in data])


def find_evenly_divisible_values(row):
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            current_value = row[i]
            next_value = row[j]
            if current_value % next_value == 0:
                return current_value / next_value
            if next_value % current_value == 0:
                return next_value / current_value


def corruption_checksum_2(data):
    return sum(
        find_evenly_divisible_values(row)
        for row in data
    )


if __name__ == '__main__':
    data = load_data()
    print(corruption_checksum(data))
    print(corruption_checksum_2(data))
