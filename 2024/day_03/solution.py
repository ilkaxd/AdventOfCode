import os
import re


def find_muls(data: str, second: bool = False) -> int:
    regex = r"mul\(\d{1,3},\d{1,3}\)"
    if second:
        regex += r"|don't\(\)|do\(\)"
    operations = re.findall(regex, data)
    result = 0
    enable = True
    for operation in operations:
        if operation == "don't()":
            enable = False
        elif operation == "do()":
            enable = True
        else:
            first, second = map(int, re.findall("\d{1,3}", operation))
            if enable:
                result += first * second
    return result


def load_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, 'input.txt')) as f:
        return f.read()


if __name__ == "__main__":
    data = load_data()
    print(find_muls(data))
    print(find_muls(data, True))
