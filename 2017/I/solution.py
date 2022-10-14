class Group:
    def __init__(self, score, children, parent):
        self.score = score
        self.children = children
        self.parent = parent


def load_data():
    with open(r'2017\I\input.txt') as f:
        return [
            x
            for x in f.read().split('\n')
            if x != ''
        ][0]


def calculate_score(group, result=0):
    result += group.score
    for child in group.children:
        result = calculate_score(child, result)
    return result


def stream_processing(data):
    """
    На вход подаётся строка, состоящая из 2 типов элементов:
        - групп - начинаются { и заканчиваются }
        - мусор - начинаются < и заканчиваются >
    Всё что считается мусором не учитывается
    В строке также имеется символ !, после которого
    стоит элемент, который никак не учитывается
    Каждая группа имеет своё значение
    Внешняя группа равна 1, группа в группе равна 1 и т.д.
    Необходимо подсчитать общий счёт
    """
    is_garbage = False
    ignore = False
    clean_data = ''
    # Чистим данные
    for ch in data:
        if ignore:
            ignore = False
            continue
        if ch == '!':
            ignore = True
            continue
        if ch == '>' and is_garbage:
            is_garbage = False
            continue
        if ch != '>' and is_garbage:
            continue
        if ch == '<' and not is_garbage:
            is_garbage = True
            continue
        if ch == ',':
            continue
        clean_data += ch

    root = None
    score = 1

    root = Group(score, [], None)
    for ch in clean_data[1:-1]:
        if ch == '{':
            score += 1
            new_child = Group(score, [], root)
            root.children.append(new_child)
            root = new_child
        else:
            score -= 1
            root = root.parent
    result = calculate_score(root)
    return result


def stream_processing_2(data):
    is_garbage = False
    ignore = False
    clean_data = ''
    result = 0
    # Чистим данные
    for ch in data:
        if ignore:
            ignore = False
            continue
        if ch == '!':
            ignore = True
            continue
        if ch == '>' and is_garbage:
            is_garbage = False
            continue
        if ch != '>' and is_garbage:
            result += 1
            continue
        if ch == '<' and not is_garbage:
            is_garbage = True
            continue
        if ch == ',':
            continue
        clean_data += ch
    return result


if __name__ == '__main__':
    data = load_data()
    print(stream_processing(data))
    print(stream_processing_2(data))
