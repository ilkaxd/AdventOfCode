def load_data():
    with open(r'2015\L_12\input.txt') as f:
        return f.read()


def count_values(dictionary):
    """
    Имеется структура данных, похожая на JSON
    необходимо найти сумму всех чисел
    """
    if isinstance(dictionary, int):
        return dictionary
    if isinstance(dictionary, dict):
        return sum(count_values(v) for v in dictionary.values())
    if isinstance(dictionary, list):
        return sum(count_values(x) for x in dictionary)
    # Если состоит только из строки
    return 0


def count_values_2(dictionary):
    """
    Если во вложенном словаре есть red,
    то мы его пропускаем
    """
    if isinstance(dictionary, int):
        return dictionary
    if isinstance(dictionary, dict):
        if 'red' in dictionary.values():
            return 0
        return sum(count_values_2(v) for v in dictionary.values())
    if isinstance(dictionary, list):
        return sum(count_values_2(x) for x in dictionary)
    # Если состоит только из строки
    return 0


if __name__ == '__main__':
    data = eval(load_data())
    print(count_values(data))
    print(count_values_2(data))
