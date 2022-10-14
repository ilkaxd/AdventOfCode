class Node:
    def __init__(self, value, previous_node=None, next_node=None):
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node


def load_data():
    with open(r'2018\I_09\input.txt') as f:
        row = f.readline().split()
        return int(row[0]), int(row[6])


def marble_mania(players_count, high_score):
    players = [0 for _ in range(players_count)]
    player_idx = 0
    current_node = Node(0)
    current_node.next_node = current_node
    current_node.previous_node = current_node
    lowest_number = 1
    while lowest_number < high_score:
        if lowest_number % 23 == 0:
            players[player_idx] += lowest_number
            for _ in range(7):
                current_node = current_node.previous_node
            players[player_idx] += current_node.value
            previous_node = current_node.previous_node
            next_node = current_node.next_node
            previous_node.next_node = next_node
            next_node.previous_node = previous_node
            current_node = next_node
        else:
            next_node = current_node.next_node
            next_next_node = next_node.next_node
            node = Node(lowest_number, next_node, next_next_node)
            next_node.next_node = node
            next_next_node.previous_node = node
            current_node = node

        lowest_number += 1
        player_idx = (player_idx + 1) % players_count
    return max(players)


if __name__ == '__main__':
    players, finish = load_data()
    print(marble_mania(players, finish * 100))
