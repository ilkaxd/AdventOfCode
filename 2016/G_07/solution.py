import re


def load_data():
    with open(r'2016\G_07\input.txt') as f:
        return f.readlines()


def ABBA(parts):
    for part in parts:
        for i in range(len(part) - 3):
            first = part[i]
            second = part[i + 1]
            third = part[i + 2]
            forth = part[i + 3]
            if first == forth and second == third and first != second:
                return True
    return False


def support_TLS(row):
    '''
    Строка правильная, если за пределами скобок
    есть подстрока ABBA, а в скобках такой строки нет
    '''
    regex_1 = re.compile(r'\[\w+\]')
    bad_parts = regex_1.findall(row)
    right_string = row
    for part in bad_parts:
        right_string = right_string.replace(part, ' ')
    right_parts = right_string.split(' ')

    condition_1 = ABBA(right_parts)
    condition_2 = ABBA(bad_parts)

    return condition_1 and not condition_2


def ABA(parts):
    result = []
    for part in parts:
        for i in range(len(part) - 2):
            first = part[i]
            second = part[i + 1]
            third = part[i + 2]
            if first != second and first == third:
                result.append(part[i:i+3])
    return result


def ABA_BAD(value, array):
    for local in array:
        if value[0] == local[1] and value[1] == local[0]:
            return True
    return False


def support_SSL(row):
    '''
    Строка правильная, если в скобках есть последовательность
    BAB, а за пределами скобок ABA
    '''
    regex_1 = re.compile(r'\[\w+\]')
    bad_parts = regex_1.findall(row)
    right_string = row
    for part in bad_parts:
        right_string = right_string.replace(part, ' ')
    right_parts = right_string.split(' ')
    condition_1 = ABA(right_parts)
    condition_2 = ABA(bad_parts)
    return any(ABA_BAD(value, condition_2) for value in condition_1)


def count_TLS(data):
    result = 0
    for row in data:
        if support_TLS(row.rstrip('\n')):
            result += 1
    return result


def count_SSL(data):
    result = 0
    for row in data:
        if support_SSL(row.rstrip('\n')):
            result += 1
    return result


if __name__ == '__main__':
    data = load_data()
    print(count_TLS(data))
    print(count_SSL(data))
