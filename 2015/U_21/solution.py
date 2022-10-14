from enum import Enum
from copy import deepcopy


class ItemType(Enum):
    WEAPON = 1
    ARMOR = 2
    RING = 3

    def __str__(self):
        current = super().__str__()
        if current == 'ItemType.WEAPON':
            return 'WEAPON'
        if current == 'ItemType.ARMOR':
            return 'ARMOR'
        if current == 'ItemType.RING':
            return 'RING'

    def __repr__(self):
        current = super().__repr__()
        if current == 'ItemType.WEAPON':
            return 'WEAPON'
        if current == 'ItemType.ARMOR':
            return 'ARMOR'
        if current == 'ItemType.RING':
            return 'RING'


class Item:
    def __init__(self, name, cost, damage, armor, itemType):
        self.name = name 
        self.cost = cost
        self.damage = damage
        self.armor = armor
        self.itemType = itemType

    def __str__(self):
        return (
            f'{self.name} ({self.itemType}) ' +
            f'Cost: {self.cost}, Damage: {self.damage}, Armor: {self.armor}'
        )

    def __repr__(self):
        return self.__str__()


class Player:
    def __init__(
        self,
        weapon=None, armor=None, rings=[],
        base_damage=0, base_hitpoints=0, base_armor=0
    ):
        self.weapon = weapon
        self.armor = armor
        self.rings = rings
        self.base_damage = base_damage
        self.hitpoints = base_hitpoints
        self.base_armor = base_armor

    def get_attack(self):
        result = self.base_damage
        if self.weapon is not None:
            result += self.weapon.damage
        if self.armor is not None:
            result += self.armor.damage
        if self.rings != []:
            result += sum(
                ring.damage
                for ring in self.rings
                if ring is not None
            )
        return result

    def get_armor(self):
        result = self.base_armor
        if self.weapon is not None:
            result += self.weapon.armor
        if self.armor is not None:
            result += self.armor.armor
        if self.rings != []:
            result += sum(
                ring.armor
                for ring in self.rings
                if ring is not None
            )
        return result

    def get_cost(self):
        result = 0
        if self.weapon is not None:
            result += self.weapon.cost
        if self.armor is not None:
            result += self.armor.cost
        if self.rings != []:
            result += sum(
                ring.cost
                for ring in self.rings
                if ring is not None
            )
        return result

    def defend(self, damage):
        armor = self.get_armor()
        self.hitpoints -= max(damage - armor, 1)

    def is_lose(self):
        if self.hitpoints <= 0:
            return True
        return False

    def fight(self, enemy):
        while True:
            # мы атакуем
            enemy.defend(self.get_attack())
            if enemy.is_lose():
                return True
            # мы защищаемся
            self.defend(enemy.get_attack())
            if self.is_lose():
                return False

    def __str__(self):
        return (
            f'Damage: {self.get_attack()}, Armor: {self.get_armor()}, ' +
            f'Cost: {self.get_cost()}, Heatbox: {self.hitpoints}'
        )

    def __repr__(self):
        return self.__str__()


def load_data():
    with open(r'2015\U\input.txt') as f:
        return [x for x in f.read().split('\n') if x != '']


def find_best_equipment(shop, enemy):
    '''
    Играем в PVP и ищем комбинацию самую дешёвую
    комбинацию снаряжения для победы и самую дорогую
    для проигрыша
    '''
    costs_win = []
    costs_lose = []
    for weapon in shop['weapons']:
        for armor in [None] + shop['armors']:
            for left_ring in [None] + shop['rings']:
                for right_ring in [None] + shop['rings']:
                    if right_ring is not None and right_ring == left_ring:
                        continue
                    player = Player(
                        weapon, armor, [left_ring, right_ring],
                        base_hitpoints=100
                    )
                    if player.fight(deepcopy(enemy)):
                        costs_win.append(player.get_cost())
                    else:
                        costs_lose.append(player.get_cost())

    return min(costs_win), max(costs_lose)


if __name__ == '__main__':
    data = load_data()
    shop = {
        'weapons': [
            Item(
                'Dagger',
                cost=8, damage=4, armor=0,
                itemType=ItemType.WEAPON
            ),
            Item(
                'Shortsword',
                cost=10, damage=5, armor=0,
                itemType=ItemType.WEAPON
            ),
            Item(
                'Warhammer',
                cost=25, damage=6, armor=0,
                itemType=ItemType.WEAPON
            ),
            Item(
                'Longsword',
                cost=40, damage=7, armor=0,
                itemType=ItemType.WEAPON
            ),
            Item(
                'Greataxe',
                cost=74, damage=8, armor=0,
                itemType=ItemType.WEAPON
            ),
        ],
        'armors': [
            Item(
                'Leather',
                cost=13, damage=0, armor=1,
                itemType=ItemType.ARMOR
            ),
            Item(
                'Chainmail',
                cost=31, damage=0, armor=2,
                itemType=ItemType.ARMOR
            ),
            Item(
                'Splintmail',
                cost=53, damage=0, armor=3,
                itemType=ItemType.ARMOR
            ),
            Item(
                'Bandedmail',
                cost=75, damage=0, armor=4,
                itemType=ItemType.ARMOR
            ),
            Item(
                'Platemail',
                cost=102, damage=0, armor=5,
                itemType=ItemType.ARMOR
            ),
        ],
        'rings': [
            Item(
                'Damage +1',
                cost=25, damage=1, armor=0,
                itemType=ItemType.RING
            ),
            Item(
                'Damage +2',
                cost=50, damage=2, armor=0,
                itemType=ItemType.RING
            ),
            Item(
                'Damage +3',
                cost=100, damage=3, armor=0,
                itemType=ItemType.RING
            ),
            Item(
                'Defense +1',
                cost=20, damage=0, armor=1,
                itemType=ItemType.RING
            ),
            Item(
                'Defense +2',
                cost=40, damage=0, armor=2,
                itemType=ItemType.RING
            ),
            Item(
                'Defense +3',
                cost=80, damage=0, armor=3,
                itemType=ItemType.RING
            ),
        ],
    }
    enemy = Player(
        base_hitpoints=int(data[0].split(':')[1]),
        base_damage=int(data[1].split(':')[1]),
        base_armor=int(data[2].split(':')[1]),
    )
    print(find_best_equipment(shop, enemy))
