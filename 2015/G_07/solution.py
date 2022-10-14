def load_data():
    with open(r'2015\G_07\input.txt') as f:
        return f.read()


def parse_value(operator, values):
    if operator.isdecimal():
        return int(operator)
    return values[operator]


def BitwiseOperations(instructions):
    """
    Выполняем битовые операции для указанных выражений
    """
    values = {}
    isUsed = [False] * len(instructions)
    while sum(isUsed) != len(instructions):
        for i, instruction in enumerate(instructions):
            try:
                if not isUsed[i]:
                    left, right = instruction.split(' -> ')
                    if left.startswith('NOT'):
                        operator = left.replace('NOT ', '')
                        operator = parse_value(operator, values)
                        values[right] = 65536 + ~operator
                    elif 'AND' in left:
                        x, y = left.split(' AND ')
                        x = parse_value(x, values)
                        y = parse_value(y, values)
                        values[right] = x & y
                    elif 'OR' in left:
                        x, y = left.split(' OR ')
                        x = parse_value(x, values)
                        y = parse_value(y, values)
                        values[right] = x | y
                    elif 'LSHIFT' in left:
                        x, y = left.split(' LSHIFT ')
                        x = parse_value(x, values)
                        y = parse_value(y, values)
                        values[right] = x << y
                    elif 'RSHIFT' in left:
                        x, y = left.split(' RSHIFT ')
                        x = parse_value(x, values)
                        y = parse_value(y, values)
                        values[right] = x >> y
                    else:
                        values[right] = parse_value(left, values)
                    isUsed[i] = True
            except:
                continue
    return values


if __name__ == '__main__':
    data = [x for x in load_data().split('\n') if x != '']
    result = BitwiseOperations(data)['a']
    print(result)
    data = [f'{result} -> b' if x.endswith('-> b') else x for x in data]
    print(BitwiseOperations(data)['a'])
