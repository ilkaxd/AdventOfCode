import string


class Queue:
    def __init__(self, size):
        self.data = list(string.ascii_lowercase[:size])
        self.head = 0
        self.size = size

    def spin(self, shift):
        self.head = (self.size + self.head - shift) % self.size

    def exchange(self, a_idx, b_idx):
        a_idx = (a_idx + self.head) % self.size
        b_idx = (b_idx + self.head) % self.size
        self.data[a_idx], self.data[b_idx] = self.data[b_idx], self.data[a_idx]

    def partner(self, a, b):
        a_idx = self.data.index(a)
        b_idx = self.data.index(b)
        self.data[a_idx], self.data[b_idx] = self.data[b_idx], self.data[a_idx]

    def __str__(self) -> str:
        return ''.join(self.data[self.head:]) + ''.join(self.data[:self.head])


def load_data():
    with open(r'2017\P_16\input.txt') as f:
        return f.readline().rstrip('\n').split(',')


def write_file(data):
    with open(r'2017\P_16\test.txt', 'w') as f:
        f.write('\n'.join(data))


def permutation_promenade(data, programms):
    for row in data:
        if row.startswith('s'):
            programms.spin(int(row[1:]))
        elif row.startswith('x'):
            row = row[1:]
            a_idx, b_idx = map(int, row.split('/'))
            programms.exchange(a_idx, b_idx)
        elif row.startswith('p'):
            row = row[1:]
            a, b = row.split('/')
            programms.partner(a, b)


def permutation_promenade_сyclical(data, size=16, repeated=1):
    programms = Queue(size)
    initial_string = str(programms)
    i = 0
    while i < repeated:
        i += 1
        permutation_promenade(data, programms)
        if initial_string == str(programms):
            break

    if repeated < i:
        return str(programms)
    repeated = repeated % i
    for _ in range(repeated):
        permutation_promenade(data, programms)
    return str(programms)


if __name__ == '__main__':
    data = load_data()
    size = 16

    print(permutation_promenade_сyclical(data, size, 1))
    print(permutation_promenade_сyclical(data, size, 1_000_000_000))
