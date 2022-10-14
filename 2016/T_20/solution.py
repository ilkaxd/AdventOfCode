def load_data():
    with open(r'2016\T_20\input.txt') as f:
        return f.readlines()


def merge_limits(x, y):
    if x[1] + 1 < y[0]:
        return (y[0], y[1])
    return (min(x[0], y[0]), max(x[1], y[1]))


def firewall_rules(data, min_available=0, max_available=4294967295):
    """
    Данн набор ограничений, которые могут пересекаться
    ищем минимальное доступное значение
    и количество доступных значений
    """
    limits = []
    for row in data:
        low, high = map(int, row.split('-'))
        limits.append((low, high))

    limits.sort(key=lambda x: x[0])
    borders = [limits[0]]
    current = borders[0]
    for limit in limits[1:]:
        new_limit = merge_limits(current, limit)
        if new_limit == limit:
            borders.append(new_limit)
        else:
            borders[-1] = new_limit
        current = borders[-1]

    available_count = 0
    current = min_available
    for low, high in borders:
        available_count += low - current
        current = high + 1

    if borders[-1][1] < max_available:
        available_count += max_available - borders[-1][1]

    if borders[0][0] == 0:
        min_available = borders[0][1] + 1
    return min_available, available_count


if __name__ == '__main__':
    data = load_data()
    print(firewall_rules(data))
