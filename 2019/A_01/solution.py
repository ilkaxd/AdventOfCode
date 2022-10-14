def load_data():
    with open(r'2019\A_01\input.txt') as f:
        return list(map(int, f.read().strip('\n').split('\n')))


def calculate_fuel_requered(mass):
    """
    Вычисляем сколько нужно топлива для шатла по формуле:
    mass / 12 => округляем вниз и вычитаем 2
    """
    return mass // 3 - 2


def calculate_recursion_fuel_requered(mass):
    """
    Вычисляем рекурсивно,
    пока масса не станет отрицательной
    """
    result = mass // 3 - 2
    if result <= 0:
        return 0
    return result + calculate_recursion_fuel_requered(result)


if __name__ == '__main__':
    data = load_data()
    fuel = sum(map(calculate_fuel_requered, data))
    fuel_2 = sum(map(calculate_recursion_fuel_requered, data))
    print(fuel, fuel_2)
