import hashlib


def load_data():
    with open(r'2016\Q_17\input.txt') as f:
        return f.readline()


def get_hash(data):
    hash_object = hashlib.md5(data.encode())
    return hash_object.hexdigest()


def is_door_open(value):
    is_open = ['b', 'c', 'd', 'e', 'f']
    return value in is_open


def is_doors_open(data):
    hash = get_hash(data)
    # верхняя, нижняя, левая, правая
    return [is_door_open(x) for x in hash[:4]]


def _two_steps_forward(
    hash,
    x=0, y=0, target_x=3, target_y=3,
    steps='', results=[]
):
    # мы в нужной точке
    if (
        x == target_x
        and
        y == target_y
    ):
        results.append(steps)
        return results

    directions = is_doors_open(hash + steps)
    for i in range(len(directions)):
        ch = ''
        new_x = x
        new_y = y
        if i == 0:
            ch = 'U'
            new_y = y - 1
        elif i == 1:
            ch = 'D'
            new_y = y + 1
        elif i == 2:
            ch = 'L'
            new_x = x - 1
        elif i == 3:
            ch = 'R'
            new_x = x + 1
        if (
            directions[i]
            and
            0 <= new_x <= target_x
            and
            0 <= new_y <= target_y
        ):
            results = _two_steps_forward(
                hash,
                new_x, new_y, target_x, target_y,
                steps + ch, results
            )
    return results


def two_steps_forward(hash):
    '''
    Ищем минимальный и максимальный пути
    из верхней левой точки в правую нижнюю
    Доступности пути определяется первыми 4 символами MD5 хеша
    '''
    paths = _two_steps_forward(hash, results=[])
    return min(paths, key=len), len(max(paths, key=len))


if __name__ == '__main__':
    data = load_data()
    print(two_steps_forward(data))
