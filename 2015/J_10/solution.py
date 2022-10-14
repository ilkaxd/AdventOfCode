def load_data():
    with open(r'2015\J_10\input.txt') as f:
        return f.readline().strip('\n')


def look_and_say(sequence):
    count = 0
    value = sequence[0]
    result = ''
    for ch in sequence:
        if ch == value:
            count += 1
        else:
            result += f'{count}{value}'
            count = 1
            value = ch
    result += f'{count}{value}'
    return result


def look_and_say_repeat(sequence, n=40):
    for _ in range(n):
        sequence = look_and_say(sequence)
    return len(sequence)


if __name__ == '__main__':
    data = load_data()
    print(look_and_say_repeat(data))
    print(look_and_say_repeat(data, 50))
