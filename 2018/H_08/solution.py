def load_data():
    with open(r'2018\H_08\input.txt') as f:
        return list(map(int, f.readline().split()))


class Node:
    def __init__(self, data):
        self.children_count = next(data)
        self.metadata_count = next(data)
        self.children = [Node(data) for _ in range(self.children_count)]
        self.metadata = [next(data) for _ in range(self.metadata_count)]
        if self.children_count == 0:
            self.value = sum(self.metadata)
        else:
            self.value = 0
            for i in self.metadata:
                i -= 1
                if i < self.children_count:
                    self.value += self.children[i].value

    def sum_metadata(self):
        result = sum(self.metadata)
        for child in self.children:
            result += child.sum_metadata()
        return result


def string_generator(data):
    for ch in data:
        yield ch


def memory_maneuver(data):
    node = Node(string_generator(data))
    return node.sum_metadata(), node.value


if __name__ == '__main__':
    data = load_data()
    print(memory_maneuver(data))
