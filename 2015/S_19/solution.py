import re


def load_data():
    with open(r'2015\S_19\input.txt') as f:
        return [x for x in f.read().split('\n') if x != '']


def medicine_for_Rudolpf(data):
    """
    Ищем количество уникальных строк,
    полученных при единичной замене
    """
    molecule = data[-1]
    results = []
    for replacement in data[:-1]:
        first, second = replacement.split(' => ')
        for start_idx in [m.start() for m in re.finditer(first, molecule)]:
            left_part = molecule[:start_idx]
            rigth_part = molecule[start_idx + len(first):]
            new_string = left_part + second + rigth_part
            results.append(new_string)
    return len(set(results))


def make_sequences(current, target, i, steps, replacements):
    if current == target:
        steps.append(i)
        return
    if len(current) > len(target):
        return
    for key in replacements.keys():
        for m in re.finditer(key, current):
            start_idx = m.start()
            left_part = current[:start_idx]
            rigth_part = current[start_idx + len(key):]
            for value in replacements[key]:
                new_molecule = left_part + value + rigth_part
                make_sequences(
                    new_molecule,
                    target, i + 1, steps, replacements
                )


def medicine_for_Rudolpf_2(data):
    """
    Ищем минимальное количество преобразований,
    необходимых для перехода от e к целевой молекуле
    """
    lines = data
    medicine = lines[-1].strip()
    replacements = [(t.split()[-1], t.split()[0]) for t in lines if '=>' in t]
    replacements = replacements[::-1]
    total = 0
    while medicine != 'e':
        for lhs, rhs in replacements:
            if lhs in medicine:
                medicine = medicine.replace(lhs, rhs, 1)
                total += 1
                break
    return total


if __name__ == '__main__':
    data = load_data()
    print(medicine_for_Rudolpf(data))
    print(medicine_for_Rudolpf_2(data))
