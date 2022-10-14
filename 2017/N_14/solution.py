def load_data():
    with open(r'2017\N_14\input.txt') as f:
        return f.readline()


if __name__ == '__main__':
    data = load_data()
    print(data)
