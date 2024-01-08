def load_data():
    with open(r'2023\E\input.txt') as f:
        return f.readlines()


if __name__ == '__main__':
    data = load_data()
    print(data)
