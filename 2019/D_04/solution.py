def load_data():
    with open(r'2019\D_04\input.txt') as f:
        return map(int, f.readline().split('-'))


def double_values(value):
    value = str(value)
    for i in range(len(value) - 1):
        first = value[i]
        second = value[i + 1]
        if first == second:
            return True
    return False


def increace_numbers(value):
    value = str(value)
    for i in range(len(value) - 1):
        first = value[i]
        second = value[i + 1]
        if first > second:
            return False
    return True


def double_values_2(value):
    value = str(value)
    memory = [value[0]]

    for i in range(1, len(value)):
        first = value[i]
        second = memory[-1]
        if first == second:
            memory.append(first)
        else:
            if len(memory) == 2:
                return True
            else:
                memory = [first]
    if len(memory) == 2:
        return True
    return False


def find_password_count(min_value, max_value):
    '''
    Ищем числа из указанного диапазона, которое:
        - имеет 2 одинаковые цифры рядом: 22 в 122345
        - числа идут в неубывающем порядке: 111123
    '''
    result = []
    result_2 = []
    for value in range(min_value, max_value + 1):
        if double_values(value) and increace_numbers(value):
            result.append(value)
        if double_values_2(value) and increace_numbers(value):
            result_2.append(value)
    return len(result), len(result_2)


if __name__ == '__main__':
    min_value, max_value = load_data()
    print(find_password_count(min_value, max_value))
