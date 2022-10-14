def load_data():
    with open(r'2018\Q_17\input.txt') as f:
        return f.read()


if __name__ == '__main__':
    data = load_data()
    print(data)
