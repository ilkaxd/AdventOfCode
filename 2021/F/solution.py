def load_data():
    with open(r'2021\F\input.txt') as f:
        return list(map(int, f.readline().split(',')))


def lanternfisf(data, n=80):
    '''
    Реализуем экспоненциальный рост стаи рыб
    после n количества дней
    '''
    fish = [data.count(i) for i in range(9)]
    for _ in range(n):
        num = fish.pop(0)
        fish[6] += num
        fish.append(num)
    return sum(fish)


if __name__ == '__main__':
    data = load_data()
    print(lanternfisf(data))
    print(lanternfisf(data, 256))
