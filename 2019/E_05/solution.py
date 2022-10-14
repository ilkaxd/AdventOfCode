def load_data():
    with open(r'2019\E_05\input.txt') as f:
        return list(map(int, f.readline().split(',')))


def TEST_actions(actions, memory=1):
    '''
    Проходим по массиву чисел, представленных набором команд и значений
    команды выглядит следующим образом
    ABCDE
    DE - индекс команды
    C - режим первой переменной
    B - режим второй переменной
    A - режим вывода

    Поддерживаемые команды:
        - 01 - сумма
        - 02 - умножение
        - 03 - ввод значения переменной a в ячейку с индексом b
        - 04 - вывод значений b или значение в ячейке b
        - 05 - переходим в ячейку с индексом b, если a != 0
        - 06 - переходим в ячейку с индексом c, если a != 0
        - 07 - в ячейку записываем 1, если a меньше b
        - 08 - в ячейку записываем 1, если a = b

    Поддерживаемые режимы переменных:
        - 0 - берём значение из ячейки с указанным индексом
        - 1 - берём само значение
    '''
    actions = actions.copy()
    add_command = '01'
    multiply_command = '02'
    input_command = '03'
    output_command = '04'
    jump_if_true_command = '05'
    jump_if_false_command = '06'
    less_than_command = '07'
    equals_command = '08'
    posistion_mode = '0'
    halt_command = 99

    result = []
    i = 0
    while actions[i] != halt_command:
        action = actions[i]
        action = str(action).rjust(4, '0')

        opcode = action[2:]
        if opcode == input_command:
            actions[actions[i + 1]] = memory
            i += 2
            continue
        if opcode == output_command:
            value = (
                actions[actions[i + 1]]
                if action[1] == posistion_mode
                else actions[i + 1]
            )
            result.append(value)
            i += 2
            continue

        first_parameter_mode, second_parameter_mode = action[1], action[0]
        (
            first_parameter, second_parameter, idx
        ) = actions[i + 1], actions[i + 2], actions[i + 3]
        if first_parameter_mode == posistion_mode:
            first_parameter = actions[first_parameter]
        if second_parameter_mode == posistion_mode:
            second_parameter = actions[second_parameter]

        if opcode == add_command:
            actions[idx] = first_parameter + second_parameter
            i += 4
        if opcode == multiply_command:
            actions[idx] = first_parameter * second_parameter
            i += 4
        if opcode == jump_if_true_command:
            i = second_parameter if first_parameter != 0 else i + 3
        if opcode == jump_if_false_command:
            i = second_parameter if first_parameter == 0 else i + 3
        if opcode == less_than_command:
            actions[idx] = 1 if first_parameter < second_parameter else 0
            i += 4
        if opcode == equals_command:
            actions[idx] = 1 if first_parameter == second_parameter else 0
            i += 4

    return result[-1]


if __name__ == '__main__':
    data = load_data()
    print(TEST_actions(data, 1))
    print(TEST_actions(data, 5))
