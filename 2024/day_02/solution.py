import os
import re


def count_safe(data: list[list[int]], second=False) -> int:
    result = 0
    for value in data:
        is_safe, idx = is_safe_check(value)
        if is_safe:
            result += 1
        else:
            if second:
                if try_to_fix(value, idx):
                    result += 1
    return result


def try_to_fix(data: list[int], idx: int) -> bool:
    for delta in (-1, 0, 1):
        # Чтобы не ушли меньше 0
        if delta == -1 and idx == 0:
            continue

        # Чтобы не ушли за пределы массива
        if delta == 1 and idx == len(data) - 1:
            continue

        new_data = data[:idx + delta] + data[idx + delta + 1:]
        is_safe, _ = is_safe_check(new_data)
        if is_safe:
            return True
    return False


def is_safe_check(data: list[int]) -> bool:
    direction = None
    for i in range(len(data) - 1):
        first, second = data[i], data[i + 1]
        delta = second - first
        if not 0 < abs(delta) < 4:
            return False, i
        delta_direction = delta / abs(delta)
        if direction is None:
            direction = delta_direction
        else:
            if delta_direction != direction:
                return False, i

    return True, None


def load_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = []
    with open(os.path.join(dir_path, 'input.txt')) as f:
        for line in f.readlines():
            data.append(list(map(int, re.findall('(\w+)', line))))
    return data


if __name__ == '__main__':
    data = load_data()
    print(count_safe(data))
    print(count_safe(data, True))
