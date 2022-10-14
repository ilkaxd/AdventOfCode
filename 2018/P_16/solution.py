def load_data():
    with open(r'2018\P_16\input.txt') as f:
        return f.read()


def addition_registry(inputs, A_inputs, B_inputs, output):
    inputs[output] = inputs[A_inputs] + inputs[B_inputs]


def addition_immediate(inputs, A_inputs, B_inputs, output):
    inputs[output] = inputs[A_inputs] + B_inputs


def multiplication_registry(inputs, A_inputs, B_inputs, output):
    inputs[output] = inputs[A_inputs] * inputs[B_inputs]


def multiplication_immediate(inputs, A_inputs, B_inputs, output):
    inputs[output] = inputs[A_inputs] * B_inputs


def bitwise_and_registry(inputs, A_inputs, B_inputs, output):
    inputs[output] = inputs[A_inputs] & inputs[B_inputs]


def bitwise_and_immediate(inputs, A_inputs, B_inputs, output):
    inputs[output] = inputs[A_inputs] & B_inputs


def bitwise_or_registry(inputs, A_inputs, B_inputs, output):
    inputs[output] = inputs[A_inputs] | inputs[B_inputs]


def bitwise_or_immediate(inputs, A_inputs, B_inputs, output):
    inputs[output] = inputs[A_inputs] | B_inputs


def assigment_register(inputs, A_inputs, B_inputs, output):
    inputs[output] = inputs[A_inputs]



def assigment_immediate(inputs, A_inputs, B_inputs, output):
    inputs[output] = A_inputs


def greater_than_im_reg(inputs, A_inputs, B_inputs, output):
    inputs[output] = 1 if A_inputs > inputs[B_inputs] else 0


def greater_than_reg_im(inputs, A_inputs, B_inputs, output):
    inputs[output] = 1 if inputs[A_inputs] > B_inputs else 0


def greater_than_reg_reg(inputs, A_inputs, B_inputs, output):
    inputs[output] = 1 if inputs[A_inputs] > inputs[B_inputs] else 0


def equality_im_reg(inputs, A_inputs, B_inputs, output):
    inputs[output] = 1 if A_inputs == inputs[B_inputs] else 0


def equality_reg_im(inputs, A_inputs, B_inputs, output):
    inputs[output] = 1 if inputs[A_inputs] == B_inputs else 0


def equality_reg_reg(inputs, A_inputs, B_inputs, output):
    inputs[output] = 1 if inputs[A_inputs] == inputs[B_inputs] else 0


def get_simple_key(available_functions):
    for key, value in available_functions.items():
        if len(value) == 1:
            return key, list(value)[0]
    return None, None


def chronal_classification(data):
    first, second = data.split('\n\n\n\n')
    batches = first.split('\n\n')
    opcodes_count = {
        'addr': (addition_registry, []),
        'addi': (addition_immediate, []),
        'mulr': (multiplication_registry, []),
        'muli': (multiplication_immediate, []),
        'banr': (bitwise_and_registry, []),
        'bani': (bitwise_and_immediate, []),
        'borr': (bitwise_or_registry, []),
        'bori': (bitwise_or_immediate, []),
        'setr': (assigment_register, []),
        'seti': (assigment_immediate, []),
        'gtir': (greater_than_im_reg, []),
        'gtri': (greater_than_reg_im, []),
        'gtrr': (greater_than_reg_reg, []),
        'eqir': (equality_im_reg, []),
        'eqri': (equality_reg_im, []),
        'eqrr': (equality_reg_reg, []),
    }
    result_matches = 0
    for batch in batches:
        before, instruction, after = (batch.split('\n'))
        before_data = list(map(int, before.split(': ')[1][1:-1].split(', ')))
        after_data = list(map(int, after.split(':  ')[1][1:-1].split(', ')))
        instruction = list(map(int, instruction.split(' ')))
        opcode, A, B, C = instruction
        opcodes_match_count = 0
        for (func, history) in opcodes_count.values():
            try:
                inputs = [x for x in before_data]
                func(inputs, A, B, C)
                if inputs == after_data:
                    opcodes_match_count += 1
                    history.append(opcode)
            except:
                continue
        if opcodes_match_count >= 3:
            result_matches += 1

    function_opcode_matches = {}
    available_functions = {}

    for key, (_, value) in opcodes_count.items():
        available_functions[key] = list(set(value))

    while any(x != [] for x in available_functions.values()):
        func, idx = get_simple_key(available_functions)
        function_opcode_matches[idx] = func
        for value in available_functions.values():
            if idx in value:
                value.remove(idx)
    result = [0, 0, 0, 0]
    for instruction in second.split('\n'):
        if instruction == '':
            continue
        opcode, A, B, C = list(map(int, instruction.split()))
        func_name = function_opcode_matches[opcode]
        func = opcodes_count[func_name][0](result, A, B, C)
    return result_matches, result


if __name__ == '__main__':
    data = load_data()
    print(chronal_classification(data))
