from collections import Counter


def load_data():
    with open(r'2018\B_02\input.txt') as f:
        return [x for x in f.read().split('\n') if x != '']


def frequency_exists(target, dictionary):
    for value in dictionary.values():
        if value == target:
            return True
    return False


def check_frequency(row):
    """
    Возвращаем 1, 1, если в строке есть 
    ровно 2 повторения некоторого символа
    и
    ровно 3 повторения некоторого символа
    """
    first = 0
    second = 0
    frequencies = Counter(row)
    if frequency_exists(2, frequencies):
        first = 1
    if frequency_exists(3, frequencies):
        second = 1
    return first, second


def inventory_management_system(data):
    first = 0
    second = 0
    for row in data:
        first_delta, second_delta = check_frequency(row)
        first += first_delta
        second += second_delta
    return first * second


def compare_strings(data):
    """
    Ищем строки, которые отличаются 1 символом
    """
    for i in range(len(data)):
        X = data[i]
        for j in range(i, len(data)):
            Y = data[j]
            delta = 0
            result = ''
            for n in range(len(X)):
                if X[n] != Y[n]:
                    delta += 1
                else:
                    result += X[n]
            if delta == 1:
                return result


if __name__ == '__main__':
    data = load_data()
    print(inventory_management_system(data))
    print(compare_strings(data))
