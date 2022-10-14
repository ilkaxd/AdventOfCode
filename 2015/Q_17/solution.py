def load_data():
    with open(r'2015\Q_17\input.txt') as f:
        return [int(x) for x in f.read().split('\n') if x != '']


def fill_refregirator(
    available_containers,
    volume=0,
    result=0, target_volume=150
):
    """
    Считаем количество возможных сечетаний,
    сумма элементов которых меньше target_volume
    """
    if volume == target_volume:
        return result + 1
    if volume > target_volume:
        return result
    for i in range(len(available_containers)):
        result = fill_refregirator(
            available_containers[i + 1:],
            volume + available_containers[i],
            result,
            target_volume
        )

    return result


def generate_sequences(
    available_containers,
    volume=0,
    sequence=[],
    result=[],
    target_volume=150
):
    """
    Считаем количество возможных сечетаний,
    сумма элементов которых меньше target_volume
    """
    if volume == target_volume:
        result.append(sequence)
        return result
    if volume > target_volume:
        return result
    for i in range(len(available_containers)):
        container = available_containers[i]
        sub_sequence = sequence.copy()
        sub_sequence.append(container)
        result = generate_sequences(
            available_containers[i + 1:],
            volume + container,
            sub_sequence,
            result,
            target_volume
        )

    return result


def min_needed(data, target=150):
    combinations = generate_sequences(
        data,
        target_volume=target
    )
    min_length = len(min(combinations, key= lambda x: len(x)))
    result = [len(x) == min_length for x in combinations]
    return sum(result)


if __name__ == '__main__':
    data = load_data()
    print(fill_refregirator(data))
    print(min_needed(data))
