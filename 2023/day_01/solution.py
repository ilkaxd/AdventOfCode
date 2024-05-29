import os
import re


def load_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, 'input.txt')) as f:
        return [x.rstrip('\n') for x in f.readlines()]


def trebuchet(data, first=True):
    result = 0

    if first:
        regex = r'\d'
    else:
        regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'

    for row in data:
        digits = re.findall(regex, row)
        value = str_to_digit(digits[0], 10) + str_to_digit(digits[-1])
        result += value
    return result


def str_to_digit(value, multiplier=1):
    match value:
        case 'one':
            return 1 * multiplier
        case 'two':
            return 2 * multiplier
        case 'three':
            return 3 * multiplier
        case 'four':
            return 4 * multiplier
        case 'five':
            return 5 * multiplier
        case 'six':
            return 6 * multiplier
        case 'seven':
            return 7 * multiplier
        case 'eight':
            return 8 * multiplier
        case 'nine':
            return 9 * multiplier
        case _:
            return int(value) * multiplier


if __name__ == '__main__':
    data = load_data()
    print(trebuchet(data))
    print(trebuchet(data, False))
