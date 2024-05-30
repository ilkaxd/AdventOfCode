import os


class Card:
    def __init__(self, card_row):
        card_description, only_numbers = card_row.split(':')
        self.card_number = int(card_description.split()[1])
        winning, having = only_numbers.split('|')
        self.winning_list = list(map(int, winning.split()))
        self.having_list = list(map(int, having.split()))
        self.cards_count = 0

    def get_concurence(self):
        concurrence = 0
        for having in self.having_list:
            if having in self.winning_list:
                concurrence += 1
        return concurrence

    def get_score(self):
        concurrence = self.get_concurence()
        if concurrence > 0:
            return 2 ** (concurrence - 1)
        return 0

    def get_cards_count(self, cards):
        if self.cards_count != 0:
            return self.cards_count
        result = 1
        concurrence = self.get_concurence()

        card_indexes = list(
            range(
                self.card_number + 1,
                self.card_number + concurrence + 1
            )
        )

        for card_index in card_indexes:
            if card_index in cards.keys():
                result += cards[card_index].get_cards_count(cards)

        self.cards_count = result

        return result


def load_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, 'input.txt')) as f:
        return f.readlines()


def scratchcards(cards_list):
    result_1 = 0
    result_2 = 0

    cards = {}

    for card_raw in cards_list:
        card = Card(card_raw)
        cards[card.card_number] = card

    for card_index in cards.keys():
        card = cards[card_index]
        result_1 += card.get_score()
        result_2 += card.get_cards_count(cards)

    return result_1, result_2


if __name__ == '__main__':
    data = load_data()
    print(scratchcards(data))
