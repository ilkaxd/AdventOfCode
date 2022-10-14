def load_data():
    with open(r'2018\E_05\input.txt') as f:
        return f.readline().strip('\n')


def alchemical_reductuion(data):
    '''
    Последовательно удаляем пары вида aA и bB.
    Считаем количество оставшихся значений
    '''
    changed = True
    delta = ord('a') - ord('A')
    while changed:
        changed = False
        for i in range(len(data) - 1):
            current = ord(data[i])
            next = ord(data[i + 1])
            if abs(current - next) == delta:
                data = data[:i] + data[i + 1 + 1:]
                changed = True
                break
    return len(data)


def alchemical_reductuion_2(data):
    '''
    Ищем символ, удаление которого
    приведёт к наименьшей длине последовательности
    '''
    return min([
        alchemical_reductuion(
            data.replace(value, '').replace(value.upper(), '')
        )
        for value in set(data.lower())
    ])


if __name__ == '__main__':
    data = load_data()

    print(alchemical_reductuion(data))
    print(alchemical_reductuion_2(data))
