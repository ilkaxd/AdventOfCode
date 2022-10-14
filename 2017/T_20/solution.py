def load_data():
    with open(r'2017\T_20\input.txt') as f:
        return f.readlines()


if __name__ == '__main__':
    data = load_data()
    print(data)
