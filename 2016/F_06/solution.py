from collections import Counter


def load_data():
    with open(r'2016\F_06\input.txt') as f:
        return list(map(str.rstrip, f.readlines()))


def find_common_values(data):
    '''
    В каждом столбце ищем наиболее часто встречающийся символ
    '''
    result = ''
    for i in range(len(data[0])):
        column = [row[i] for row in data]
        counter = Counter(column)
        temp = counter.most_common(1)
        result += temp[0][0]
    return result


def find_least_common_values(data):
    '''
    В каждом столбце ищем наименее часто встречающийся символ
    '''
    result = ''
    for i in range(len(data[0])):
        column = [row[i] for row in data]
        counter = Counter(column)
        temp = min(counter.items(), key=lambda x: x[1])
        result += temp[0][0]
    return result


if __name__ == '__main__':
    data = load_data()
    print(find_common_values(data))
    print(find_least_common_values(data))
