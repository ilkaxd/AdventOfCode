def load_data():
    with open(r'2019\G_07\input.txt') as f:
        return list(map(int, f.readline().split(',')))


if __name__ == '__main__':
    data = load_data()
    # print(data)
    data = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    print(sum(data))
