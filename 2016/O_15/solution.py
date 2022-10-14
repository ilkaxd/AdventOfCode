import re
import copy


class Disc:
    def __init__(self, number, positions, position):
        self.number = number
        self.positions = positions
        self.position = position
        self.timestamp = 0

    def tick(self, steps=1):
        self.timestamp += steps
        self.position = (self.position + steps) % self.positions

    def __str__(self) -> str:
        return (
            f'Disc #{self.number} at time {self.timestamp} '
            f'in position {self.position} ({self.positions})'
        )

    def __repr__(self):
        return self.__str__()


def load_data():
    with open(r'2016\O_15\input.txt') as f:
        return [x for x in f.readlines() if x != '']


def disc_parse(row):
    regex = re.compile(
        r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).'
    )
    groups = map(int, regex.search(row).groups())
    return groups


def tick_discs(discs, shift=1):
    for i in range(len(discs)):
        discs[i].tick(shift)


def fall_capsule(discs, shift=0):
    # Ждём
    tick_discs(discs, shift)
    # Падаем
    for capsule_position in range(len(discs)):
        tick_discs(discs)
        disc = discs[capsule_position]
        if disc.position != 0:
            return False
    return True


def timing_is_everything(rows, new_disc=False):
    '''
    Имеются диски, который имеют n позиций
    и которые находятся в m-ной позиции
    Нужно найти момент времени, при котором
    диски выстраиваются в таком порядке,
    что при проходе от первого до последнего
    на каждом шаге диск находится в позиции 0
    '''
    discs = []
    for row in rows:
        disc = Disc(*disc_parse(row))
        discs.append(disc)

    if new_disc:
        discs.append(Disc(len(rows) + 1, 11, 0))

    shift = 0
    while True:
        new_discs = [copy.copy(x) for x in discs]
        if fall_capsule(new_discs, shift):
            return shift
        shift += 1


if __name__ == '__main__':
    data = load_data()
    print(timing_is_everything(data))
    print(timing_is_everything(data, True))
