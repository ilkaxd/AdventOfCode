import re


def load_data():
    with open(r'2015\W\input.txt') as f:
        return [x for x in f.read().split('\n') if x != '']


def use_register(instructions, a=0, b=0):
    registers = {
            'a': a,
            'b': b
        }

    regex_1 = re.compile(r'[a-z]{3}')
    regex_2 = re.compile(r' ([ab]{1})')
    regex_3 = re.compile(r'[+\-0-9]+')

    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        command = regex_1.findall(instruction)[0]
        register = regex_2.findall(instruction)
        offset = regex_3.findall(instruction)
        if command == 'hlf':
            registers[register[0]] /= 2
        elif command == 'tpl':
            registers[register[0]] *= 3
        elif command == 'inc':
            registers[register[0]] += 1
        elif command == 'jmp':
            i += int(offset[0])
            continue
        elif command == 'jie':
            if registers[register[0]] % 2 == 0:
                i += int(offset[0])
                continue
        elif command == 'jio':
            if registers[register[0]] == 1:
                i += int(offset[0])
                continue
        i += 1
    return registers['b']


if __name__ == '__main__':
    data = load_data()
    print(use_register(data, a=0, b=0))
    print(use_register(data, a=1, b=0))
