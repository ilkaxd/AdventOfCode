def load_data():
    with open(r'2016\L_12\input.txt') as f:
        return f.readlines()


def make_instructions(instructions, init_value=0):
    '''
    Есть 4 регистра:
        a инициируется 0
        b инициируется 0
        c инициируется init_value
        d инициируется 0

    Выполняем инструкции:
        cpy x y - копирует значение или значение регистра x в регистр y
        inc x - инкрементирует значение регистра x
        dec x - декрементирует значение регистра x
        jnz x y - переходит на y инструкций вперёд
        если значение или значение регистра x не равно 0
    Возвращаем значение регистра a
    '''
    registers = {
        'a': 0,
        'b': 0,
        'c': init_value,
        'd': 0
    }
    i = 0
    while i < len(instructions):
        instruction = instructions[i].rstrip('\n')
        if instruction.startswith('cpy'):
            value, target = instruction.split()[1:]
            if value.isdigit():
                registers[target] = int(value)
            else:
                registers[target] = registers[value]
        elif instruction.startswith('inc'):
            target = instruction.split()[1]
            registers[target] += 1
        elif instruction.startswith('dec'):
            target = instruction.split()[1]
            registers[target] -= 1
        elif instruction.startswith('jnz'):
            condition_idx, value = instruction.split()[1:]
            if condition_idx.isdigit():
                condition = int(condition_idx)
            else:
                condition = registers[condition_idx]
            if condition != 0:
                i += int(value)
                continue
        i += 1
    return registers['a']


if __name__ == '__main__':
    data = load_data()
    print(make_instructions(data))
    print(make_instructions(data, init_value=1))
