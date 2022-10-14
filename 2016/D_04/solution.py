from collections import Counter
from operator import itemgetter


def load_data():
    with open(r'2016\D_04\input.txt') as f:
        return f.read().split('\n')[:-1]


def is_real_room(row):
    """
    Комната реальна, если пять наиболее часто
    встречающихся символов в строке соответствуют
    чек-сумме (указана в скобках)
    Если у имеет место одинаковая частота, то символы
    сортируются в алфавитном порядке
    """
    splitted = row.split('-')
    letters = ''.join(splitted[:-1])
    sector_id, check_sum = splitted[-1].split('[')
    check_sum = check_sum.strip('[]')
    counter = Counter(letters).items()
    counter = sorted(counter, reverse=False, key=lambda x: x[0])
    counter = sorted(counter, reverse=True, key=itemgetter(1))
    most_common = ''.join(x for x, _ in counter[:5])
    return most_common == check_sum, int(sector_id)


def count_real_room(data):
    result = 0
    for x in data:
        condition, sector_id = is_real_room(x)
        if condition:
            result += sector_id
    return result


def decrypt(row):
    '''
    Декодирование шифра Цезаря
    '''
    result = ''
    high = ord('z') + 1
    low = ord('a')
    delta = high - low
    id = int(row.split('-')[-1])
    shift = id % delta
    for ch in row[:-3]:
        if ch == '-':
            result += ' '
        else:
            new_simbol = ord(ch) + shift
            if new_simbol >= high:
                new_simbol -= delta
            result += chr(new_simbol)
    return result.rstrip(' '), id


def find_id(data, target):
    for row in data:
        row, id = decrypt(row[:-7])
        if row == target:
            return id


if __name__ == '__main__':
    data = load_data()
    print(count_real_room(data))
    print(find_id(data, 'northpole object storage'))
