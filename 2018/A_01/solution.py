def load_data():
    with open(r'2018\A_01\input.txt') as f:
        return [int(x) for x in f.read().split('\n') if x != '']


def sum_all(data):
    """
    Просто всё суммируем
    """
    return sum(data)


def find_repeted_value(data):
    """
    Ищем значение которое после суммы встречается повторно
    список цикличен
    """
    visited = [0]
    x = 0
    while True:
        for value in data:
            x += value
            if x in visited:
                return x
            visited.append(x)


if __name__ == '__main__':
    data = load_data()
    print(sum_all(data))
    print(find_repeted_value(data))
