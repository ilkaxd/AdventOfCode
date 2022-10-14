import hashlib


def load_data():
    with open(r'2016\E_05\input.txt') as f:
        return f.readline()


def find_password(door_id):
    '''
    Ищем хеш от MD5, который начинается с 5 нулей
    6 символ в хеше будет символом пароля
    длинна пароля равна 8
    '''
    result = ''
    id = 0
    while len(result) != 8:
        string = f'{door_id}{id}'.encode()
        hash = hashlib.md5(string).hexdigest()
        if hash[:5] == '00000':
            result += hash[5]
        id += 1
    return result


def find_password_2(door_id):
    '''
    6 символ указывает на позицию в пароле
    7 символ является символом пароля
    отбрасываются все неподходящие позиции
    сохраняется только первое вхождение
    '''
    result = [None for _ in range(8)]
    id = 0
    while any([value is None for value in result]):
        string = f'{door_id}{id}'.encode()
        hash = hashlib.md5(string).hexdigest()
        if hash[:5] == '00000':
            position = hash[5]
            value = hash[6]
            if position.isdigit():
                position = int(position)
                if 0 <= position < len(result):
                    if result[position] is None:
                        result[position] = value
        id += 1
    return ''.join(result)


if __name__ == '__main__':
    data = load_data()
    print(find_password(data))
    print(find_password_2(data))
