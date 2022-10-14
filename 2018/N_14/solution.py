def load_data():
    with open(r'2018\N_14\input.txt') as f:
        return f.readline()


def combine(a, b):
    result = a + b
    if result >= 10:
        return [result // 10, result % 10]
    return [result % 10]


def print_chart(data, idx_a, idx_b):
    result = ''
    for i in range(len(data)):
        if i == idx_a:
            result += f'({data[i]})'
        elif i == idx_b:
            result += f'[{data[i]}]'
        else:
            result += f' {data[i]} '
    print(result)


def chocolate_charts(size):
    score_board, a_idx, b_idx = [3, 7], 0, 1

    while len(score_board) < size + 10:
        a = score_board[a_idx]
        b = score_board[b_idx]

        score_board += combine(a, b)

        a_idx = (a_idx + 1 + a) % len(score_board)
        b_idx = (b_idx + 1 + b) % len(score_board)

        # print_chart(score_board, a_idx, b_idx)
    return ''.join(map(str, score_board[size:size + 10]))


def chocolate_charts_backward(target):
    score_board, a_idx, b_idx = [3, 7], 0, 1
    size = len(target)
    target = list(map(int, target))

    while (
        (score_board[-size:] != target)
        and
        (score_board[-size-1:-1] != target)
    ):
        a = score_board[a_idx]
        b = score_board[b_idx]

        score_board += combine(a, b)

        a_idx = (a_idx + 1 + a) % len(score_board)
        b_idx = (b_idx + 1 + b) % len(score_board)
    return len(score_board) - size


if __name__ == '__main__':
    data = load_data()
    print(chocolate_charts(int(data)))
    print(chocolate_charts_backward(data))
