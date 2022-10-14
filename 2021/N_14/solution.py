from collections import Counter


def load_data():
    with open((r'2021\N_14\input.txt')) as f:
        return [x.rstrip('\n') for x in f.readlines()]


def extended_polymerization(data, iterations=10):
    template = data[0]
    rules = dict(x.split(' -> ')for x in data[2:])
    a, b = 0, 0
    for idx in range(iterations):
        if idx < 10:
            new_template = template[0]
            for i in range(len(template) - 1):
                pair = template[i:i+2]
                middle = rules.get(pair, '')
                new_template += (middle + pair[1])
            template = new_template
            c = Counter(template).most_common(len(set(template)))
            a, b = c[0][1], c[-1][1]
        else:
            a *= 2
            b *= 2

    return a - b


if __name__ == '__main__':
    data = load_data()
    data = [
        'NNCB',
        '',
        'CH -> B',
        'HH -> N',
        'CB -> H',
        'NH -> C',
        'HB -> C',
        'HC -> B',
        'HN -> C',
        'NN -> C',
        'BH -> H',
        'NC -> B',
        'NB -> B',
        'BN -> B',
        'BB -> N',
        'BC -> B',
        'CC -> N',
        'CN -> C',
    ]
    print(extended_polymerization(data, 40))