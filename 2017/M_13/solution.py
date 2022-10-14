import copy


class Layer:
    def __init__(self, number, depth):
        self.number = number
        self.depth = depth
        self.direction = 1
        self.position = 0

    def step(self):
        if self.position == (self.depth - 1):
            self.direction = -1
        elif self.position == 0:
            self.direction = 1
        self.position += self.direction

    def get_position_by_delay(self, delay):
        self.position = (self.position + self.depth)

    def __str__(self):
        return ''.join(
            '[ ]'
            if i != self.position else '[S]'
            for i in range(self.depth)
        )


def load_data():
    with open(r'2017\M_13\input.txt') as f:
        return f.readlines()


def all_step(layers):
    for layer in layers:
        layer.step()


def count_detections(layers, delay = 0):
    step = 0
    last_step = max(layers.keys())
    for _ in range(delay):
        all_step(layers.values())
    result = []
    while step <= last_step:
        layer = layers.get(step)
        if layer is not None and layer.position == 0:
            result.append(step * layer.depth)
        all_step(layers.values())
        step += 1
    return result


def packet_scanners(data):
    layers = {}
    for row in data:
        layer_number, depth = map(int, row.split(':'))
        layers[layer_number] = Layer(layer_number, depth)

    result = count_detections(copy.deepcopy(layers), 0)

    delay = 1
    while count_detections(copy.deepcopy(layers), delay) != []:
        delay += 1

    layer = layers[4]
    for i in range(10):
        print(i, '->', layer.position)
        layer.step()

    delay = 7
    temp = 0
    if delay // (layer.depth - 1) == 0:
        temp = delay % layer.depth
    else:
        temp = (layer.depth - 1) - delay % (layer.depth - 1)
    print(temp)

    return sum(result), delay


if __name__ == '__main__':
    data = load_data()
    data = [
        '0: 3',
        '1: 2',
        '4: 4',
        '6: 4'
    ]
    print(packet_scanners(data))
