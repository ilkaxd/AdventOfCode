def load_data():
    with open(r'2017\E\input.txt') as f:
        return [
            int(x)
            for x in f.read().split('\n')
            if x != ''
        ]


def twisty_trampolines(data):
    """
    Проходим по списку, в котором указаны смещения
    относительно текущего положения
    после каждого просмотра смещения мы увеличиваем его
    на 1. Необходимо найти количество шагов, прежде чем
    мы выйдем из цикла
    """
    i = previous_i = 0
    steps = 0
    while i < len(data):
        steps += 1
        offset = data[i]
        i += offset
        data[previous_i] += 1
        previous_i = i
    return steps


def twisty_trampolines_2(data):
    """
    Теперь если смещение >= 3, то мы
    уменьшаем смещение на 1. В противном случае
    увеличиваем на 1
    """
    i = previous_i = 0
    steps = 0
    while i < len(data):
        steps += 1
        offset = data[i]
        i += offset
        if offset >=3:
            data[previous_i] -= 1
        else:
            data[previous_i] += 1
        previous_i = i
    return steps


if __name__ == '__main__':
    data = load_data()
    print(twisty_trampolines(data.copy()))
    print(twisty_trampolines_2(data.copy()))
