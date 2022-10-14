class Queue:
    def __init__(self, idx):
        self.idx = idx
        self.prev = None
        self.next = None

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev


def load_data():
    with open(r'2016\S_19\input.txt') as f:
        return int(f.readline())


def make_elfs(size):
    elfs = [Queue(i + 1) for i in range(size)]

    for i in range(size):
        elfs[i].next = elfs[(i + 1) % size]
        elfs[i].prev = elfs[(i - 1) % size]
    return elfs


def elephant_named_joseph(size):
    """
    Обнуляем следующий элемент
    """
    elfs = make_elfs(size)
    current = elfs[0]
    while current.next is not None:
        neighbor = current.next.next
        current.next = None if neighbor.idx == current.idx else neighbor
        current = neighbor
    return current.idx


def elephant_named_joseph_2(size):
    """
    Обнуляем элемент напротив
    """
    elfs = make_elfs(size)
    current, across = elfs[0], elfs[size // 2]
    while current != across:
        across.remove()
        across = across.next
        if size % 2 == 1:
            across = across.next
        size -= 1
        current = current.next
    return current.idx


if __name__ == '__main__':
    data = load_data()
    print(elephant_named_joseph(data))
    print(elephant_named_joseph_2(5))
