class Spell:
    def __init__(
        self,
        cost=0,
        damage=0, armor=0,
        heal=0, manaheal=0,
        duration=1
    ):
        self.cost = cost
        self.damage = damage
        self.heal = heal
        self.duration = duration
        self.armor = armor
        self.manaheal = manaheal


class Player:
    available_spells = {
            'Magic_Missile': Spell(cost=53, damage=4),
            'Drain': Spell(cost=73, damage=2, heal=2),
            'Shield': Spell(cost=113, duration=6, armor=7),
            'Poison': Spell(cost=173, duration=6, damage=3),
            'Recharge': Spell(cost=229, duration=5, manaheal=101)
        }

    def __init__(
        self,
        damage=0, base_hitpoints=0,
        base_armor=0,
        mana=0
    ):
        self.damage = damage
        self.hitpoints = base_hitpoints
        self.mana = mana
        self.base_armor = base_armor
        self.effects = []

    def __str__(self):
        return (
            f'Damage: {self.damage} '
            f'Heatbox: {self.hitpoints}'
        )

    def __repr__(self):
        return self.__str__()

    def is_spell_anable(self, spell):
        if spell.cast > self.mana:
            return True
        return False

    def is_alive(self):
        return self.hitpoints > 0

    def cast(self, spell, enemy):
        self.effects_tick()
        enemy.effects_tick()
        # Эффект можно скаставать ещё раз
        spell = self.available_spells[spell]
        # Моментальный спел
        if spell.duration == 0:
            enemy.defend(spell.damage)
            self.hitpoints += spell.heal
            self.mana -= spell.cost
        # периодический урон боссу
        elif spell.damage != 0:
            boss.effects.append(spell)
        # бафф себе
        else:
            self.effects.append(spell)

    def defend(self, damage):
        armor = self.base_armor
        self.hitpoints -= max(damage - armor, 1)

    def fight(self, enemy, spells=[]):
        for spell in spells:
            self.defend(enemy.damage)

    def effects_tick(self):
        for effect in self.effects:
            pass

    def melee_attack(self, enemy):
        self.effects_tick()
        enemy.effects_tick()
        enemy.defend(self.damage)


def load_data():
    with open(r'2015\V_22\input.txt') as f:
        return f.read().split('\n')


def game(player, boss):
    # while player.is_alive() and boss.is_alive():
    #     # Игрок атакует
    #     # Босс атакует

    boss.melee_attack(player)


if __name__ == '__main__':
    data = load_data()
    hitbox = int(data[0].split(':')[1])
    damage = int(data[1].split(':')[1])
    # player = Player(base_hitpoints=50, mana=500)
    # boss = Player(base_hitpoints=hitbox, damage=damage)
    player = Player(base_hitpoints=10, mana=250)
    boss = Player(base_hitpoints=13, damage=8)
    print(game(player, boss))
