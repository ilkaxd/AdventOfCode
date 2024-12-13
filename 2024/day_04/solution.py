import os


def find_word(data: list[list[str]]) -> int:
    grid_width = len(data[0])
    grid_height = len(data)

    result = 0
    word = "XMAS"
    word_length = len(word)
    for y in range(grid_height):
        for x in range(grid_width):
            for x_delta, y_delta in (
                (-1, -1),
                (0, -1),
                (1, -1),
                (-1, 0),
                (1, 0),
                (-1, 1),
                (0, 1),
                (1, 1)
            ):
                # Проверяем границы
                if (
                    (0 <= x + x_delta * (word_length - 1) <= grid_width - 1)
                    and
                    (0 <= y + y_delta * (word_length - 1) <= grid_height - 1)
                ):
                    find_word = ""
                    for i in range(word_length):
                        new_x = x + x_delta * i
                        new_y = y + y_delta * i
                        find_word += data[new_y][new_x]
                    if find_word == word:
                        result += 1
    return result


def find_word_2(data: list[list[str]]) -> int:
    word_1 = [
        ['M', '.', 'S'],
        ['.', 'A', '.'],
        ['M', '.', 'S']
    ]
    word_2 = [
        ['M', '.', 'M'],
        ['.', 'A', '.'],
        ['S', '.', 'S']
    ]
    word_3 = [
        ['S', '.', 'M'],
        ['.', 'A', '.'],
        ['S', '.', 'M']
    ]
    word_4 = [
        ['S', '.', 'S'],
        ['.', 'A', '.'],
        ['M', '.', 'M']
    ]
    grid_width = len(data[0])
    grid_height = len(data)

    result = 0

    for y in range(grid_height):
        for x in range(grid_width):
            if (
                (0 < x < grid_width - 1)
                and
                (0 < y < grid_height - 1)
            ):
                area = [data[y + delta_y][x-1:x+1+1] for delta_y in (-1, 0, 1)]
                if x == 6 and y == 2:
                    pass
                for word in (word_1, word_2, word_3, word_4):
                    if (
                        (area[0][0] == word[0][0])
                        and
                        (area[0][2] == word[0][2])
                        and
                        (area[1][1] == word[1][1])
                        and
                        (area[2][0] == word[2][0])
                        and
                        (area[2][2] == word[2][2])
                    ):
                        result += 1
    return result


def load_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, 'input.txt')) as f:
        return [list(line.replace('\n', '')) for line in f.readlines()]


if __name__ == "__main__":
    data = load_data()
    print(find_word(data))
    print(find_word_2(data))
