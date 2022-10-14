def load_data():
    with open(r'2018\O_15\input.txt') as f:
        return [list(x.rstrip('\n')) for x in f.readlines()]


def parse_grid(grid):
    wall = '#'
    cavern = '.'
    goblin = 'G'
    elf = 'E'


if __name__ == '__main__':
    data = load_data()
    print(data)
