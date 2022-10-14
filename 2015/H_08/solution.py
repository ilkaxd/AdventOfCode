import re


def load_data():
    with open(r'2015\H_08\input.txt') as f:
        return f.read()


def CountSimbols(rows):
    """
    Считаем количество символов в строке и в памяти
    """
    characters_of_code = 0
    characters_of_data = 0
    for row in rows:
        characters_of_code += len(row)
        row = row[1:-1]
        row = row.replace(r'\\', 'a')
        simbols = re.findall(r'\\x..', row)
        for simbol in simbols:
            row = row.replace(simbol, 'a')
        row = row.replace('\\', '')
        characters_of_data += len(row)
    return characters_of_code - characters_of_data


def CountRawSimbols(rows):
    """
    Каждый специальный символ снабжаем /
    """
    characters_of_code = 0
    encoded_characters = 0
    for row in rows:
        characters_of_code += len(row)
        row = row[1:-1]
        encoded_characters += (3 + 3)
        for ch in row:
            if ch == '"' or ch == '\\':
                encoded_characters += 1
            encoded_characters += 1
    return encoded_characters - characters_of_code


if __name__ == '__main__':
    data = [x for x in load_data().split('\n') if x != '']
    print(CountSimbols(data))
    print(CountRawSimbols(data))
