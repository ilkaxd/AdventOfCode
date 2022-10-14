def load_data():
    with open(r'2017\J\input.txt') as f:
        return [int(x) for x in f.readline().split(',')]


def knot_hash(inputs, lengths):
    """
    На вход подаётся массив из чисел (inputs)
    и массив из размером подмассивов (lengths)
    Необходимо пройти по всем lengths и выполнить следующие действия:
        - развернуть подмассив, который начинается с current_position,
        указанного размера
        - увеличить current_position на размер подмассива + смещение
        - увеличить смещение на 1
    Вернуть произведение первого и второго элементов массива
    """
    current_position = 0
    skip_size = 0

    inputs_size = len(inputs)

    for length in lengths:
        end_position = current_position + length
        subset = []
        for i in range(current_position, end_position):
            subset.append(inputs[i % inputs_size])
        subset = subset[::-1]
        for j, i in enumerate(range(current_position, end_position)):
            inputs[i % inputs_size] = subset[j]
        current_position = (
            current_position + length + skip_size
            ) % inputs_size
        skip_size += 1
    return inputs[0] * inputs[1]


def modify_array(inputs):
    result = []
    ending = [17, 31, 73, 47, 23]
    for value in ','.join(map(str, inputs)):
        result.append(ord(value))
    return result + ending


def knot_hash_2():
    pass


if __name__ == '__main__':
    data = load_data()
    inputs = list(range(256))
    print(knot_hash(inputs.copy(), data))

    inputs = modify_array(inputs)
