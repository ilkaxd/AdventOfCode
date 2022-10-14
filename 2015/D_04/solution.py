import hashlib


def load_data():
    with open(r'2015\D_04\input.txt') as f:
        return f.read()


def checkHash(hash, count):
    if hash.startswith('0' * count):
        return True
    return False


def findMinimumHash(secret, count):
    """
    Ищем минимальное число, которое при добавлении к секретному слову
    и хеширования по MD5 вернёт хещ с минимум первыми count нулей
    """
    result = 0
    while True:
        string = f'{secret}{result}'
        hash = hashlib.md5(string.encode()).hexdigest()
        if checkHash(hash, count):
            return result
        result += 1


if __name__ == '__main__':
    data = load_data()
    print(findMinimumHash(data, 5))
    print(findMinimumHash(data, 6))
