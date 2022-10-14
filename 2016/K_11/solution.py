import re


class Element:
    def __init__(self, name, type):
        self.name = name[:1].upper()
        self.type = type[:1].upper()

    def is_fried(self, other):
        if other.type == 'G' and other.name != self.name:
            return True
        return False

    def copy(self):
        return Element(self.name, self.type)

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type

    def __str__(self):
        return self.name + self.type

    def __repr__(self):
        return self.name + self.type


class Floor:
    def __init__(self, number, elements):
        self.number = number
        self.elements = elements
        self.elevator = False
        self.elevator_inner = []

    def is_saved(self):
        generators = [e for e in self.elements if e.type == 'G']
        chips = [e for e in self.elements if e.type == 'M']

        if len(generators) > 0:
            for chip in chips:
                if all(chip.is_fried(generator) for generator in generators):
                    return False
        return True

    def count_elements(self):
        return len(self.elements)

    def copy(self):
        new_floor = Floor(self.number, [])
        new_floor.elements = [el.copy() for el in self.elements]
        new_floor.elevator = self.elevator
        new_floor.elevator_inner = [el.copy() for el in self.elevator_inner]
        return new_floor

    def __eq__(self, other):
        return (
            self.number == other.number
            and
            all(el in other.elements for el in self.elements)
            and
            self.elevator == other.elevator
            and
            all(el in other.elevator_inner for el in self.elevator_inner)
        )

    def __str__(self, max_elements=0):
        dot_count = max_elements - self.count_elements()
        all_elements = self.elements + ['.'] * dot_count
        elevator = 'E' if self.elevator else '.'
        return (
            f'F{self.number} {elevator}\t' +
            '\t'.join(str(e) for e in all_elements)
        )

    def __repr__(self):
        return self.__str__()


class Building:
    def __init__(self):
        self.floors = []
        self.elevator_floor = 0

    def count_elements(self):
        return sum(floor.count_elements() for floor in self.floors)

    def add_floor(self, floor):
        self.floors.append(floor)

    def set_elevator_floor(self, floor_number):
        old_floor = self.get_elevator_floor()
        for i in range(len(self.floors)):
            if i == floor_number:
                self.floors[i].elevator = True
            else:
                self.floors[i].elevator = False
        self.elevator_floor = floor_number
        floor = self.get_elevator_floor()
        floor.elements += old_floor.elevator_inner
        old_floor.elevator_inner = []

    def move_elevator(self, direction):
        next_floor = self.elevator_floor + direction
        if 0 <= next_floor < len(self.floors):
            self.set_elevator_floor(next_floor)
        else:
            floor = self.get_elevator_floor()
            floor.elements += floor.elevator_inner
            floor.elevator_inner = []

    def is_all_elements_on_last_floor(self):
        max_elements = self.count_elements()
        return self.floors[-1].count_elements() == max_elements

    def is_saved(self):
        return all(floor.is_saved() for floor in self.floors)

    def get_available_elements(self):
        return self.floors[self.elevator_floor].elements

    def get_elevator_floor(self):
        return self.floors[self.elevator_floor]

    def pool_elements_in_elevetor(self, elems):
        floor = self.get_elevator_floor()
        floor.elevator_inner = elems
        for el in elems:
            floor.elements.remove(el)

    def __eq__(self, other):
        return (
            self.floors == other.floors
            and
            self.elevator_floor == other.elevator_floor
        )

    def copy(self):
        new_building = Building()
        new_building.floors = [floor.copy() for floor in self.floors]
        new_building.elevator_floor = self.elevator_floor
        return new_building

    def __str__(self):
        elements_count = sum(floor.count_elements() for floor in self.floors)
        return '\n'.join(
            floor.__str__(elements_count) for floor in self.floors[::-1]
        )

    def __repr__(self):
        return self.__str__()


def load_data():
    with open(r'2016\K_11\input.txt') as f:
        return f.readlines()


def GeneratorsAndMicrochips(data):
    generator_regex = re.compile(r'\w+ generator')
    mecrochip_regex = re.compile(r'\w+-compatible microchip')

    building = Building()
    for i, row in enumerate(data):
        generators = [
            Element(name, 'generator')
            for name in generator_regex.findall(row)
        ]
        chips = [
            Element(name, 'microchip')
            for name in mecrochip_regex.findall(row)
        ]
        floor = Floor(i, generators + chips)
        building.add_floor(floor)

    building.set_elevator_floor(0)
    print(building)
    return DFS(building, 0)


def DFS(building, step, min_step=1e10, history=[]):
    if building in history or not building.is_saved():
        return min_step

    if building.is_all_elements_on_last_floor():
        return min(step, min_step)

    available_combinations = get_available_combinations(
        building.get_available_elements()
    )
    for direction in (-1, 1):
        for elements in available_combinations:
            new_building = building.copy()
            new_history = [state.copy() for state in history]
            new_history.append(building)
            new_building.pool_elements_in_elevetor(elements)
            new_building.move_elevator(direction)
            min_step = DFS(new_building, step + 1, min_step, new_history)
    return min_step


def get_available_combinations(lt):
    lt = [e.copy() for e in lt]
    result = []
    for i in range(len(lt)):
        result.append([lt[i]])
        for j in range(i + 1, len(lt)):
            result.append([lt[i], lt[j]])
    return result


if __name__ == '__main__':
    data = load_data()
    data = [
        'The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.',
        'The second floor contains a hydrogen generator.',
        'The third floor contains a lithium generator.',
        'The fourth floor contains nothing relevant.',
    ]
    print(GeneratorsAndMicrochips(data))
