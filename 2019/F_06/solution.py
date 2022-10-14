class Orbit:
    def __init__(self, name):
        self.name = name
        self.orbits = []

    def count_orbits(self):
        result = len(self.orbits)
        for orbit in self.orbits:
            result += orbit.count_orbits()
        return result

    def have_element(self, target):
        for element in self.orbits:
            if element == target:
                return target
            element.have_element


def load_data():
    with open(r'2019\F_06\input.txt') as f:
        return f.readlines()


def OrbitMap(orbits_str):
    orbits = {}
    for row in orbits_str:
        first_str, second_str = row.strip('\n').split(')')
        first = orbits.get(first_str, Orbit(first_str))
        second = orbits.get(second_str, Orbit(second_str))
        second.orbits.append(first)
        orbits[first_str] = first
        orbits[second_str] = second
    
    return sum(orbit.count_orbits() for orbit in orbits.values())


if __name__ == '__main__':
    data = load_data()
    data = [
        'COM)B',
        'B)C',
        'C)D',
        'D)E',
        'E)F',
        'B)G',
        'G)H',
        'D)I',
        'E)J',
        'J)K',
        'K)L',
        'K)YOU',
        'I)SAN',
    ]
    print(OrbitMap(data))
