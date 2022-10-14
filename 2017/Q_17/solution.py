class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


def spin(node, value, shift):
    new_node = Node(value)
    for _ in range(shift):
        node = node.next

    next_node = node.next
    node.next = new_node
    new_node.previous = new_node

    new_node.next = next_node
    new_node.previous = node

    return new_node


def spinlock(shift, repeats=2017, target_index=2017):
    node = Node(0)
    node.next = node
    node.previous = node
    for i in range(1, repeats + 1):
        node = spin(node, i, shift)

    while node.value != target_index:
        node = node.next
    return node.next.value


def load_data():
    with open(r'2017\Q_17\input.txt') as f:
        return int(f.readline())


if __name__ == '__main__':
    data = load_data()
    # data = 3
    for i in range(1, 100):
        print(spinlock(data, repeats=i, target_index=0))
