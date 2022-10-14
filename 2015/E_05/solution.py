import re


def load_data():
    with open(r'2015\E_05\input.txt') as f:
        return f.read()


def IsNice(string):
    """
    Строка является правильной, если в ней имеются:
        -   минимум 3 гласные ('aeiou')
        -   нет пар 'ab', 'cd', 'pq', 'xy'
        -   есть парная строка, например aa, xx
    """
    vowels = 0
    has_duplicates = False
    for i in range(1, len(string)):
        first, second = string[i - 1], string[i]
        pair = first + second
        if first in 'aeiou':
            vowels += 1
        if (pair in ['ab', 'cd', 'pq', 'xy']):
            return False
        if first == second:
            has_duplicates = True
    if string[-1] in 'aeiou':
        vowels += 1
    return vowels >= 3 and has_duplicates


def IsNice_2(string):
    """
    Строка является правильной, если в ней имеются:
        - пара любых 2 символов, которые появляются
        как минимум ещё раз в строке без перекрытия
        (не aaa, но aaaa правильная)
        - имеется хотя бы 1 символ, который повторяется ровно
        через 1 символ
    """
    rule_1 = r'(..).*\1'
    rule_2 = r'(.).\1'

    return (
        re.search(rule_1, string) is not None
        and
        re.search(rule_2, string) is not None
    )


def countNice(sequence, f):
    return sum(
        f(x)
        for x in sequence.split()
        if x != ''
    )


if __name__ == '__main__':
    data = load_data()
    print(countNice(data, IsNice))
    print(countNice(data, IsNice_2))
