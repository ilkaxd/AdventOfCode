def load_data():
    with open(r'2015\A_01\input.txt') as f:
        return f.read()


def find_floor(sequence):
    """
    Дана последовательность скобок,
    в которой:
        - "(" увеличивает результат на 1
        - ")" уменьшает результат на 1
    """
    return sum(
        1 if x == '('  else -1
        for x in sequence
        )


def find_position(sequense):
    """
    Дана последовательность скобок, нужно найти индекс,
    когда результат равен -1
    """
    basement = -1
    current_floor = 0
    result = 0
    for step in sequense:
        result += 1
        if step == '(':
            current_floor += 1
        if step == ')':
            current_floor -= 1
        if current_floor == basement:
            return result


if __name__ == '__main__':
    data = load_data()
    print(find_floor(data))
    print(find_position(data))
