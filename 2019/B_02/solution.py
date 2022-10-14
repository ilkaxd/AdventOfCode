from share_script import Intcode


def load_data():
    with open(r'2019\B_02\input.txt') as f:
        return list(map(int, f.read().split(',')))


def program_alarm(data):
    """
    Анализируем строку. Начинаем с индекса 0
    Первый элемент обозначает операцию:
        1XYZ - складываем числа, которые расположены
        в индексах X и Y и записываем в индекс Z
        2XYZ - перемножаем
        99 - точка останова
    Заменяем значение под индексом 1 на 12 и значение
    под индексом 2 на 2
    Какое значение получилось по окончанию работы программы
    в индексе 0
    """
    return Intcode(data)


def program_alarm_2(data):
    """
    Ищем пару, которая в итоге даст 19690720 на выходе
    """
    target = 19690720
    for noun in range(100):
        for verb in range(100):
            temp = data.copy()
            temp[1] = noun
            temp[2] = verb
            if program_alarm(temp) == target:
                return 100 * noun + verb


if __name__ == '__main__':
    data = load_data()
    data[1] = 12
    data[2] = 2
    print(program_alarm(data.copy()))
    print(program_alarm_2(data))
