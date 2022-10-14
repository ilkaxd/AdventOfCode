from collections import defaultdict


def load_data():
    with open(r'2017\H\input.txt') as f:
        return [
            x
            for x in f.read().split('\n')
            if x != ''
        ]


def you_like_registers(instructions):
    """
    Имеется набор инструкций, которые поступают в формате
    X операций значение if условие, например
    av inc 167 if f > -9
    - X - ячейка, к которой применяется операция
    по умолчанию X равен нулю
    - операции поддерживаются 2 видов:
        inc value: X + value
        dec value: X - value
    - условие состоит из исследуемого значения,
    оператора сравнения и числа
    Необходимо найти максимальное число после выполнения
    всех операций
    """
    registers = defaultdict(int)
    for instruction in instructions:
        (
            target, operation, value,
            _,
            condition_target, condition_operation, condition_value
        ) = instruction.split(' ')
        condition_target_value = registers[condition_target]
        condition_value = int(condition_value)
        if eval(
            f'{condition_target_value} {condition_operation} {condition_value}'
        ):
            if operation == 'dec':
                registers[target] -= int(value)
            else:
                registers[target] += int(value)
    return max(registers.values())


def you_like_registers_2(instructions):
    """
    Ищем максимальное значение, которое появлялось
    в процессе выполнения инструкций
    """
    registers = defaultdict(int)
    max_value = float('-inf')
    for instruction in instructions:
        (
            target, operation, value,
            _,
            condition_target, condition_operation, condition_value
        ) = instruction.split(' ')
        value = int(value)
        condition_target_value = registers[condition_target]
        condition_value = int(condition_value)
        if eval(
            f'{condition_target_value} {condition_operation} {condition_value}'
        ):
            new_value = 0
            if operation == 'dec':
                new_value = registers[target] - value
            else:
                new_value = registers[target] + value
            max_value = max(max_value, new_value)
            registers[target] = new_value
    return max_value


if __name__ == '__main__':
    data = load_data()
    print(you_like_registers(data))
    print(you_like_registers_2(data))
