from collections import Counter


def load_data():
    with open(r'2017\D\input.txt') as f:
        return [
            x.split(' ')
            for x in f.read().split('\n')
            if x != ''
        ]


def passphrases_count(data):
    """
    Сторка является валидной, если в ней нет
    повторяющихся фраз
    """
    return sum(
        len(row) == len(set(row))
        for row in data
    )


def check_anagram(row):
    counters = []
    for word in row:
        counters.append(Counter(word))
    for i in range(len(counters)):
        for j in range(i + 1, len(counters)):
            if counters[i] == counters[j]:
                return False
    return True


def passphrases_count_2(data):
    """
    Строка невалидна, если какое-либо
    слово может быть полностью использована для составления другого
    """
    return sum(
        check_anagram(row)
        for row in data
    )


if __name__ == '__main__':
    data = load_data()
    print(passphrases_count(data))
    print(passphrases_count_2(data))
