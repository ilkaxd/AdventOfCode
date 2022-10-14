def load_data():
    with open(r'2019\I\input.txt') as f:
        return list(map(int, f.readline().split(',')))


if __name__ == '__main__':
    data = load_data()
    print(data)
