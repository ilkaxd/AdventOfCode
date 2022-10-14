import re
from functools import reduce


class Bot:
    def __init__(self, number):
        self.number = number
        self.chips = []

    def get_values(self):
        min_value, max_value = self.chips
        self.chips = []
        return min_value, max_value

    def add_value(self, value):
        self.chips.append(value)
        self.chips.sort()

    def value_count(self):
        return len(self.chips)

    def get_multiply(self):
        return reduce(lambda x, y: x * y, self.chips)

    def __str__(self):
        chips_str = '-'.join(self.chips)
        return f'{self.number}: ({chips_str})'

    def __repr__(self):
        return self.__str__()


def load_data():
    with open(r'2016\J_10\input.txt') as f:
        return f.readlines()


def get_object(id, bots, outputs):
    object, idx = id.split()
    idx = int(idx)
    if object == 'bot':
        return bots.get(idx, Bot(idx)), True, idx
    else:
        return outputs.get(idx, Bot(idx)), False, idx


def balance_bots(data, target_low=17, target_high=61):
    '''
    Имеется набор роботов, которые передают друг другу чипы с номерами
    робот работает только если количество чипов у него равно 2

    Помимо роботов есть также outputs

    Return:
        - id робота, который первым работал с чипами с указанными номерами
        - произведение номеров чипов с первых 3 outputs
    '''
    bots = {}
    outputs = {}

    target_id = None

    regex_1 = re.compile(r'value (\d+) goes to bot (\d+)')
    regex_2 = re.compile(
        r'bot (\d+) gives low to (\w+ \d+) and high to (\w+ \d+)'
    )
    used_instruction = [False for _ in range(len(data))]

    for i, row in enumerate(data):
        mo = regex_1.findall(row)
        if mo != []:
            used_instruction[i] = True
            value, idx = map(int, mo[0])
            bot = bots.get(idx, Bot(idx))
            bot.add_value(value)
            bots[idx] = bot

    while not all(used_instruction):
        for i, row in enumerate(data):
            if not used_instruction[i]:
                mo = regex_2.findall(row)
                bot_id, low_id, high_id = mo[0]
                bot_id = int(bot_id)
                source_bot = bots.get(bot_id, Bot(bot_id))
                # Робот работает только если количество чипов равно 2
                if source_bot.value_count() != 2:
                    continue

                (
                    low_destination,
                    low_is_bot,
                    low_idx
                ) = get_object(low_id, bots, outputs)
                (
                    high_destination,
                    high_is_bot,
                    high_idx
                ) = get_object(high_id, bots, outputs)

                low_value, high_value = source_bot.get_values()

                low_destination.add_value(low_value)
                high_destination.add_value(high_value)

                if low_value == target_low and high_value == target_high:
                    target_id = bot_id

                bots[bot_id] = source_bot
                if low_is_bot:
                    bots[low_idx] = low_destination
                else:
                    outputs[low_idx] = low_destination
                if high_is_bot:
                    bots[high_idx] = high_destination
                else:
                    outputs[high_idx] = high_destination

                used_instruction[i] = True

    return (
        target_id,
        outputs[0].get_multiply() *
        outputs[1].get_multiply() *
        outputs[2].get_multiply()
    )


if __name__ == '__main__':
    data = load_data()
    print(balance_bots(data))
