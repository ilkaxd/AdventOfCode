def load_data():
    with open(r'2017\A\input.txt') as f:
        return list(map(int, f.read()))


def inverse_captcha(data):
    """
    Вычисляем сумму элементов,
    значение которых равно следующему элементу в списке
    последний элемент сравнивается с первым
    """
    result = 0
    for i in range(len(data)):
        next_i = i + 1
        if i == (len(data) - 1):
            next_i = 0
        current_digit = data[i]
        next_digit = data[next_i]
        if current_digit == next_digit:
            result += current_digit
    return result



def inverse_captcha_2(data):
    """
    Вычисляем сумму элементов,
    значение которых равно элементу в списке,
    находящемся на другом конце
    Список цикличный
    """
    result = 0
    size = len(data)
    delta = size // 2
    for i in range(size):
        next_i = (i + delta) % size
        current_digit = data[i]
        next_digit = data[next_i]
        if current_digit == next_digit:
            result += current_digit
    return result


if __name__ == '__main__':
    data = load_data()
    print(inverse_captcha(data))
    print(inverse_captcha_2(data))
