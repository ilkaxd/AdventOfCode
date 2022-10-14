def load_data():
    with open(r'2016\C_03\input.txt') as f:
        return [
            list(map(int, triangle.split()))
            for triangle in f.read().split('\n')[:-1]
        ]


def is_triangle_possible(a, b, c):
    """
    Треугольник можно построить,
    если сумма двух его любых сторон больше третьей
    """
    return a + b > c and a + c > b and b + c > a


def count_available_triangles(data):
    return sum(
        1
        for triangle in data
        if is_triangle_possible(*triangle)
    )


def count_available_triangles_2(data):
    """
    Размеры указаны не в строках а в столбцах,
    сгруппированных по 3
    """
    result = 0
    for column in range(len(data[0])):
        for i in range(0, len(data), 3):
            triangle = [row[column] for row in data[i:i + 3]]
            if is_triangle_possible(*triangle):
                result += 1
    return result


if __name__ == '__main__':
    data = load_data()
    print(count_available_triangles(data))
    print(count_available_triangles_2(data))
