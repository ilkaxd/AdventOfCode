import hashlib
import re

import sys
sys.setrecursionlimit(10000)


def load_data():
    with open(r'2016\N_14\input.txt') as f:
        return f.readline()


def get_hash(row, n=0):
    hash_object = hashlib.md5(row.encode())
    result = hash_object.hexdigest()
    if n == 0:
        return result
    return get_hash(result, n - 1)


def contain_n_duplicates(row, value='.', count=3):
    regex = re.compile('(' + value + r')\1{' + str(count - 1) + '}')
    result = regex.search(row)
    if result is None:
        return None
    else:
        return result.group()[0]


def one_time_pad(salt, n=0):
    '''
    Ищем 64 ключ, который удовлетворяет следующим условиям
    -   В ключе, который состоит из salt и индекса
    (индексация идёт с нуля, инкрементно)
    вычисляется хеш n-раз (1 или 2016) имеется строка из
    3 одинаковых символов (берётся первая такая пара)
    - В любом из следующих 1000 хешей имеется строка из
    5 повторений указанного символа
    '''
    idx = 0
    next_hashes_count = 1_000
    current_hash = get_hash(f'{salt}{idx}', n)
    next_hashes = [
        get_hash(f'{salt}{i}', n)
        for i in range(idx + 1, idx + next_hashes_count + 1)
    ]
    i = 0

    while True:
        value = contain_n_duplicates(current_hash)
        if value is not None:
            for hash in next_hashes:
                if contain_n_duplicates(hash, value, 5) is not None:
                    i += 1
                    break
        if i == 64:
            return idx
        idx += 1
        current_hash = next_hashes.pop(0)
        next_hashes.append(get_hash(f'{salt}{idx + next_hashes_count}', n))


if __name__ == '__main__':
    data = load_data()
    print(one_time_pad(data))
    print(one_time_pad(data, 2016))
