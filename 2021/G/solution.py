def load_data():
    with open(r'2021\G\input.txt') as f:
        return list(map(int, f.readline().split(',')))


def horizontal_aligment(data, target):
    '''
    Постоянный штраф за смещение
    '''
    result = 0
    for value in data:
        result += abs(target - value)
    return result


def horizontal_aligment_2(data, target):
    '''
    Линейный штраф за смещение,
    работаем с арифметическим рядом
    '''
    result = 0
    for value in data:
        result = result + (1 + abs(target - value)) / 2 * abs(target - value)
    return result


def min_horizontal_aligment(data, second=False):
    """
    Подгоняем массив к одному значению с минимальными затратами
    на перемещение
    """
    min_aligment = float('+inf')
    for target in range(min(data), max(data) + 1):
        if not second:
            aligment = horizontal_aligment(data, target)
        else:
            aligment = horizontal_aligment_2(data, target)
        min_aligment = min(aligment, min_aligment)
    return int(min_aligment)


if __name__ == '__main__':
    data = load_data()
    print(min_horizontal_aligment(data))
    print(min_horizontal_aligment(data, True))
