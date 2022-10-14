class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = {}

    def __str__(self):
        neighbours = ', '.join(
            f'{k} ({v})'
            for k, v in self.neighbours.items()
        )
        return f'{self.name}: {neighbours}'

    def __repr__(self):
        neighbours = ', '.join(
            f'{k} ({v})'
            for k, v in self.neighbours.items()
        )
        return f'{self.name}: {neighbours}'


def load_data():
    with open(r'2015\M_13\input.txt') as f:
        return [x for x in f.read().split('\n') if x != '']


def calculate_happines(table):
    result = 0
    for i in range(len(table)):
        previous_guest = table[i - 1]
        current_guest = table[i]
        next_guest = table[(i + 1) % len(table)]
        result += current_guest.neighbours[previous_guest.name]
        result += current_guest.neighbours[next_guest.name]
    return result


def make_sequence(available, sequence, result):
    """
    Генерируем все возможные комбинации с перестановкой
    """
    if available == []:
        result.append(sequence)
        return
    for i in range(len(available)):
        sub_sequence = sequence.copy()
        sub_sequence.append(available[i])
        rest = available[:i] + available[i + 1:]
        make_sequence(rest, sub_sequence, result)


def dinner_table(family):
    """
    Определяем как рассадить гостей за круглым столом
    """
    available_sequences = []
    make_sequence(family, [], available_sequences)
    return max(map(calculate_happines, available_sequences))


def make_graph(data):
    relationships = []
    for row in data:
        X, _, operation, value, _, _, _, _, _, _, Y = row.strip('.').split()
        if operation == 'gain':
            value = int(value)
        else:
            value = -int(value)
        relationships.append((X, value, Y))
    names = set(x[0] for x in relationships)
    family = []
    for name in names:
        family.append(Node(name))
    for (X, value, Y) in relationships:
        for i in range(len(family)):
            if family[i].name == X:
                family[i].neighbours[Y] = value
                break
    return family


def add_me(family):
    """
    Добавляем в список гостей себя, учтя что
    вес с любым соседом равен 0
    """
    guests = [x.name for x in family]
    name = 'ilkaxd'
    for i in range(len(family)):
        family[i].neighbours[name] = 0
    family.append(Node(name))
    for guest in guests:
        family[-1].neighbours[guest] = 0
    return family


def first(data):
    family = make_graph(data)
    return dinner_table(family)


def second(data):
    family = make_graph(data)
    family = add_me(family)
    return dinner_table(family)


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))
