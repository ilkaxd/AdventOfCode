import os
from collections import defaultdict


def find_corrects(
    updates: list[list[int]],
    rules: list[tuple[int, int]]
):
    result = 0

    rules_dict = defaultdict(list)
    for (before, after) in rules:
        rules_dict[before].append(after)

    for update in updates:
        is_correct = is_correct_check(update, rules_dict)
        if is_correct:
            result += update[len(update) // 2]
    return result


def is_correct_check(data: list[int], rules: dict[int, list[int]]):
    for i in range(len(data)):
        head = data[i]
        rule = rules[head]
        for value in data[i + 1:]:
            if value not in rule:
                return False
    return True


def load_data():
    rules = []
    updates = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, 'input.txt')) as f:
        rules_str, updates_str = f.read().split('\n\n')

        for rule in rules_str.split('\n'):
            rules.append(list(map(int, rule.split('|'))))

        for update in updates_str.split('\n'):
            if update != '':
                updates.append(list(map(int, update.split(','))))
    return updates, rules


if __name__ == '__main__':
    updates, rules = load_data()
    # left, right
    before_list = [before for before, after in rules]
    after_list = [after for before, after in rules]
    for before in before_list:
        if before not in after_list:
            print(before)
    # print(rules)
    # print(find_corrects(rules, updates))
