def load_data():
    with open(r'2015\X\input.txt') as f:
        return [int(x) for x in f.read().split('\n') if x != '']


def make_combinations(
    available,
    current_weight,
    max_weight,
    sequence,
    result
):
    if current_weight == max_weight:
        result.append(sequence)
        return result
    if current_weight > max_weight:
        return result
    for i in range(len(available)):
        weight = available[i]
        sub_sequence = sequence.copy()
        sub_sequence.append(weight)
        result = make_combinations(
            available[i + 1:],
            current_weight + weight,
            max_weight,
            sub_sequence,
            result
        )
    return result


def balance_groups(weights):
    sum_weights = sum(weights)
    weights_of_group = sum_weights / 3
    first_group = make_combinations(weights, 0, weights_of_group, [], [])
    result = []
    for group_1 in first_group:
        rest_weights = [x for x in weights if x not in group_1]
        if sum(rest_weights) == weights_of_group * 2:
            rest_combinations = make_combinations(
                rest_weights,
                0,
                weights_of_group,
                [],
                []
            )
            for group_2 in rest_combinations:
                group_3 = [x for x in rest_weights if x not in group_2]
                if sum(group_3) == weights_of_group:
                    result.append((group_1, group_2, group_3))
    min_size = len(min(result, key=lambda x: len(x[0]))[0])
    target = [x for x, _, _ in result if len(x) == min_size]
    min_product = float('inf')

    for x in target:
        product = 1
        for value in x:
            product *= value
        min_product = min(min_product, product)
    return min_product


if __name__ == '__main__':
    data = load_data()
    # data = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
    print(balance_groups(data))
