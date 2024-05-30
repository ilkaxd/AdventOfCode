import os
import re
from functools import reduce


class Digit:
    def __init__(self, start_x, end_x, y, value):
        self.value = int(value)
        self.xs = list(range(start_x, end_x))
        self.y = y
        self.nearest_elements = []

    def is_solo(self):
        return len(self.nearest_elements) == 0


class Element:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.is_energy = value == '*'
        self.nearest_digits = []

    def is_neasert(self, digit: Digit):
        for x, y in [
            (self.x - 1, self.y - 1), (self.x, self.y - 1), (self.x + 1, self.y - 1),
            (self.x - 1, self.y), (self.x + 1, self.y),
            (self.x - 1, self.y + 1), (self.x, self.y + 1), (self.x + 1, self.y + 1),
        ]:
            if x in digit.xs and y == digit.y:
                if digit not in self.nearest_digits:
                    self.nearest_digits.append(digit)
                if self not in digit.nearest_elements:
                    digit.nearest_elements.append(self)
                return True
        return False


def load_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, 'input.txt')) as f:
        return [x.rstrip('\n') for x in f.readlines()]


def gear_rotation(data):
    digit_regex = re.compile(r'\d+')
    element_regex = re.compile(r'[^\d\.]')

    digits = []
    elements = []

    for y, row in enumerate(data):
        digits += [
            Digit(match.start(), match.end(), y, match.group(0))
            for match in digit_regex.finditer(row)
        ]
        elements += [
            Element(match.start(), y, match.group(0))
            for match in element_regex.finditer(row)
        ]

    for element in elements:
        for digit in digits:
            element.is_neasert(digit)

    result_1 = 0
    for digit in digits:
        if not digit.is_solo():
            result_1 += digit.value
        else:
            print(digit.value, digit.y + 1)

    result_2 = 0
    for element in elements:
        if element.is_energy and len(element.nearest_digits) == 2:
            result_2 += reduce(
                lambda x, y: x * y.value,
                element.nearest_digits, 1
            )

    return result_1, result_2


if __name__ == '__main__':
    data = load_data()
    print(gear_rotation(data))
