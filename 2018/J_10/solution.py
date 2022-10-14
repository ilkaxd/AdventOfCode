import re


def load_data():
    with open(r'2018\J_10\input.txt') as f:
        return f.readlines()


def stars_align(data):
    regex = re.compile(r'-?\d+')
    instructions = []
    for row in data:
        x, y, x_vel, y_vel = regex.findall(row)


if __name__ == '__main__':
    data = load_data()
    print(data)
