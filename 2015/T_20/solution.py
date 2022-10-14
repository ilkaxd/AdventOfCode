from collections import defaultdict

def load_data():
    with open(r'2015\T_20\input.txt') as f:
        return int(f.readline())


def presents_count(house_number):
    """
    Ищем числа, кратные указанному числу
    """
    result = []
    step = 2 if house_number % 2 else 1
    for i in range(1, int((house_number) ** 0.5) + 1, step):
        if house_number % i == 0:
            # целевой делитель и результат деления
            result += [i, house_number // i]
    return set(result)


def infinite_elves_and_infinite_houses_min(target):
    house = 1
    while True:
        current = sum(presents_count(house)) * 10
        if current >= target:
            return house
        house += 1


def infinite_elves_and_infinite_houses_min_2(target):
    house = 1
    elves = defaultdict(int)
    while True:
        current = 0
        for elf in presents_count(house):
            if not elves[elf] >= 50:
                elves[elf] += 1
                current += elf * 11
        if current >= target:
            return house
        house += 1


if __name__ == '__main__':
    data = load_data()
    print(infinite_elves_and_infinite_houses_min(data))
    print(infinite_elves_and_infinite_houses_min_2(data))
