def load_data():
    with open(r'2016\B_02\input.txt') as f:
        return f.read().split('\n')[:-1]


class Button:
    def __init__(self, number, left=None, right=None, up=None, down=None):
        self.number = number
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def go_left(self):
        if self.left is None:
            return self
        return self.left

    def go_up(self):
        if self.up is None:
            return self
        return self.up

    def go_right(self):
        if self.right is None:
            return self
        return self.right

    def go_down(self):
        if self.down is None:
            return self
        return self.down


def base_panel():
    """
    Стандартная клавиатура
    123
    456
    789
    """
    button_1 = Button('1')
    button_2 = Button('2')
    button_3 = Button('3')
    button_4 = Button('4')
    button_5 = Button('5')
    button_6 = Button('6')
    button_7 = Button('7')
    button_8 = Button('8')
    button_9 = Button('9')

    button_1.down = button_4
    button_1.right = button_2

    button_2.left = button_1
    button_2.down = button_5
    button_2.right = button_3

    button_3.left = button_2
    button_3.down = button_6

    button_4.up = button_1
    button_4.right = button_5
    button_4.down = button_7

    button_5.left = button_4
    button_5.up = button_2
    button_5.right = button_6
    button_5.down = button_8

    button_6.left = button_5
    button_6.up = button_3
    button_6.down = button_9

    button_7.up = button_4
    button_7.right = button_8

    button_8.left = button_7
    button_8.up = button_5
    button_8.right = button_9

    button_9.left = button_8
    button_9.up = button_6

    return button_5


def pretentious_panel():
    """
        1
      2 3 4
    5 6 7 8 9
      A B C
        D
    """
    button_1 = Button('1')
    button_2 = Button('2')
    button_3 = Button('3')
    button_4 = Button('4')
    button_5 = Button('5')
    button_6 = Button('6')
    button_7 = Button('7')
    button_8 = Button('8')
    button_9 = Button('9')
    button_A = Button('A')
    button_B = Button('B')
    button_C = Button('C')
    button_D = Button('D')

    button_1.down = button_3

    button_2.down = button_6
    button_2.right = button_3

    button_3.up = button_1
    button_3.left = button_2
    button_3.right = button_4
    button_3.down = button_7

    button_4.left = button_3
    button_4.down = button_8

    button_5.right = button_6

    button_6.up = button_2
    button_6.left = button_5
    button_6.right = button_7
    button_6.down = button_A

    button_7.up = button_3
    button_7.left = button_6
    button_7.right = button_8
    button_7.down = button_B

    button_8.up = button_4
    button_8.left = button_7
    button_8.right = button_9
    button_8.down = button_C

    button_9.left = button_8

    button_A.up = button_6
    button_A.right = button_B

    button_B.up = button_7
    button_B.left = button_A
    button_B.right = button_C
    button_B.down = button_D

    button_C.left = button_B
    button_C.up = button_8

    button_D.up = button_B
    return button_5


def bathroom_security(cods, panel_generator=base_panel):
    """
    Имеется клавиатура

    начинаем с цифры 5.
    Выполняем последовательность действий.
    Выходить за границы клавиатуры нельзя
    """
    result = ''
    current_number = panel_generator()
    for cod in cods:
        for action in cod:
            if action == 'U':
                current_number = current_number.go_up()
            elif action == 'L':
                current_number = current_number.go_left()
            elif action == 'D':
                current_number = current_number.go_down()
            elif action == 'R':
                current_number = current_number.go_right()
        result += current_number.number
    return result


if __name__ == '__main__':
    data = load_data()
    print(bathroom_security(data))
    print(bathroom_security(data, pretentious_panel))
