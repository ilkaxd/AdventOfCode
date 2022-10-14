def load_data():
    with open(r'2017\F\input.txt') as f:
        return [
            int(x)
            for x in f.read().split('\t')
            if x != ''
        ]


def memory_relocation(data):
    """
    На сход подаётся список, в котором сперва ищем первый
    индекс максимального элемента, обнуляем его, а это максимальное
    значение распространяем его следующим образом:
    к следующему за максимальным элементом значению мы добавляем 1
    и так по кругу, пока не раздадим всё максимальное значение
    Выполняем данный цикл, пока не появится повторяющаяся строка, 
    что свидетельствует о том, что цикл замкнулся
    """
    states = []
    steps = 0
    while True:
        steps += 1
        value = max(data)
        idx = data.index(value)
        data[idx] = 0

        for i in range(1, value + 1):
            data[(idx + i) % len(data)] += 1

        if data in states:
            return steps
        states.append(data.copy())


def memory_relocation_2(data):
    """
    мы также отслеживаем количество циклов, которое
    прошло с предыдущего повтора
    """
    states = []
    steps = 0
    while True:
        steps += 1
        value = max(data)
        idx = data.index(value)
        data[idx] = 0

        for i in range(1, value + 1):
            data[(idx + i) % len(data)] += 1

        for state, idx in states:
            if state == data:
                return steps - idx

        states.append((data.copy(), steps))


if __name__ == '__main__':
    data = load_data()
    print(memory_relocation(data))
    print(memory_relocation_2(data))
