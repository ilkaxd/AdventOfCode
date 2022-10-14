import re


class Node:
    def __init__(self, x, y, Size,  Used,  Avail,  Use):
        self.X = x
        self.Y = y
        self.InitialSize = Size
        self.UsedSize = Used
        self.AvailableSize = Avail
        self.UsedSizePercent = Use

    def IsCanFit(self, node):
        return self.AvailableSize >= node.UsedSize

    def __eq__(self, node):
        return (
            self.X == node.X
            and
            self.Y == node.Y
            and
            self.InitialSize == node.InitialSize
            and
            self.UsedSize == node.UsedSize
            and
            self.AvailableSize == node.AvailableSize
            and
            self.UsedSizePercent == node.UsedSizePercent
        )


def load_data():
    with open(r'2016\V_22\input.txt') as f:
        return f.readlines()


def grid_computing(data):
    regex = re.compile(r'\d+')
    nodes = []
    for row in data[2:]:
        x, y, Size,  Used,  Avail,  Use = map(int, regex.findall(row))
        node = Node(x, y, Size,  Used,  Avail,  Use)
        nodes.append(node)

    target_x = max(nodes, key=lambda x: x.X).X
    print(target_x)
    size = len(nodes)
    result = 0
    for i in range(size):
        for j in range(size):
            if (
                nodes[i].UsedSize != 0
                and
                nodes[i] != nodes[j]
                and
                nodes[j].IsCanFit(nodes[i])
            ):
                result += 1
    return result


if __name__ == '__main__':
    data = load_data()
    print(grid_computing(data))
