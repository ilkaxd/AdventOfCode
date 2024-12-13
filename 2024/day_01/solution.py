import os
import re
from collections import Counter


def find_distance(left_list: list[int], right_list: list[int]) -> int:
    left_list.sort()
    right_list.sort()
    result = 0
    for left_value, right_value in zip(left_list, right_list):
        delta = abs(right_value - left_value)
        result += delta
    return result


def find_similarity(left_list: list[int], right_list: list[int]) -> int:
    counter = Counter(right_list)
    return sum(counter[value] * value for value in left_list)


def load_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    left_list = []
    right_list = []
    with open(os.path.join(dir_path, 'input.txt')) as f:
        for line in f.readlines():
            left_value, right_value = map(int, re.findall('(\w+)', line))
            left_list.append(left_value)
            right_list.append(right_value)
    return left_list, right_list


if __name__ == '__main__':
    data = load_data()
    print(find_distance(*data))
    print(find_similarity(*data))
