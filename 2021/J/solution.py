def load_data():
    with open((r'2021\J\input.txt')) as f:
        return [r.rstrip('\n') for r in f.readlines()]


def is_pair(first, second):
    return get_pair(first) == second


def get_pair(ch):
    pairs = {
        '{': '}',
        '[': ']',
        '(': ')',
        '<': '>'
    }
    return pairs[ch]


def is_corrupted(row):
    memory = []
    for ch in row:
        if ch in ['(', '[', '{', '<']:
            memory.append(ch)
        else:
            previous = memory.pop()
            if not is_pair(previous, ch):
                return ch
    return memory[::-1]


def syntax_scoring(rows):
    '''
    Имеется последовательность скобок,
    ищем скобки которые имеют неправильные закрывающиеся скобки
    а неполные строки заполняем соответствующими элементами
    '''
    scoring_table = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    scoring_table_2 = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    result = 0
    result_2 = []
    for row in rows:
        corrupted_value = is_corrupted(row)
        if isinstance(corrupted_value, list):
            temp_result_2 = 0
            for ch in corrupted_value:
                temp_result_2 = temp_result_2 * 5 + scoring_table_2[
                    get_pair(ch)
                ]
            result_2.append(temp_result_2)
        else:
            result += scoring_table[corrupted_value]
    result_2.sort()

    return result, result_2[len(result_2) // 2]


if __name__ == '__main__':
    data = load_data()
    print(syntax_scoring(data))
