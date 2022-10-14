import re
from collections import Counter


class Node:
    def __init__(self, name, weight, leafs):
        self.name = name
        self.weight = weight
        self.leafs = leafs
        self.parent = None

    def __str__(self):
        return f'{self.name} ({self.weight}) -> {", ".join(self.leafs)}'

    def __repr__(self):
        return f'{self.name} ({self.weight}) -> {", ".join(self.leafs)}'


def load_data():
    with open(r'2017\G\input.txt') as f:
        return [
            x
            for x in f.read().split('\n')
            if x != ''
        ]


def make_leaf(data):
    regex = re.compile(r'\w+')
    result = regex.findall(data)
    name = result[0]
    weight = int(result[1])
    leafs = result[2:]
    return Node(name, weight, leafs)


def add_node(parent, nodes):
    for i in range(len(parent.leafs)):
        leaf = parent.leafs[i]
        for j in range(len(nodes)):
            node = nodes[j]
            if node.name == leaf:
                parent.leafs[i] = node
                nodes[j].parent = parent
                break


def calculate_weight(node):
    result = node.weight
    for leaf in node.leafs:
        result += calculate_weight(leaf)
    return result


def find_tree_root(data):
    """
    Дан список ветвей дерева,
    нужно найти его корень
    """
    nodes = []
    # Первичная подгрузка
    for row in data:
        nodes.append(make_leaf(row))
    # Построение дерева
    for i in range(len(nodes)):
        node = nodes[i]
        if node.leafs != []:
            add_node(node, nodes)

    # Поиск корня
    for node in nodes:
        if node.parent is None:
            return node.name


def other_value_in_counter(target, counter):
    for key in counter.keys():
        if target != key:
            return key


def get_key_by_value(target, dictionary):
    for key, value in dictionary.items():
        if value == target:
            return key


def tree_balance(data):
    """
    Вес каждой ветви должен быть одинаковым.
    Необходимо найти ветку, вес которой отличается
    от остальных
    """
    nodes = []
    # Первичная подгрузка
    for row in data:
        nodes.append(make_leaf(row))
    # Построение дерева
    for i in range(len(nodes)):
        node = nodes[i]
        if node.leafs != []:
            add_node(node, nodes)

    # Вычисляем суммарный вес родителя и детей
    for i in range(len(nodes)):
        node = nodes[i]
        node.accum_weight = calculate_weight(node)

    root = None
    # Вычисляем корень
    for node in nodes:
        if node.parent is None:
            root = node

    # Проходим по каждому рангу
    while True:
        nodes = [
            node 
            for node in root.leafs
        ]
        accum_weights = [
            node.accum_weight
            for node in root.leafs
        ]

        counter = Counter(accum_weights)
        abnormal_value = get_key_by_value(1, counter)
        if abnormal_value is None:
            return root.weight + previous_normal_value - previous_abnormal
        new_root = nodes[accum_weights.index(abnormal_value)]
        previous_abnormal = abnormal_value
        previous_normal_value = other_value_in_counter(abnormal_value, counter)
        root = new_root


if __name__ == '__main__':
    data = load_data()
    print(find_tree_root(data))
    print(tree_balance(data))
