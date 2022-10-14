import re
from copy import copy


class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.x_delta = 0
        self.y_delta = 0
        self.z_delta = 0

    def add_velocity(self, nearest):
        if self.x > nearest.x:
            self.x_delta -= 1
        elif self.x < nearest.x:
            self.x_delta += 1

        if self.y > nearest.y:
            self.y_delta -= 1
        elif self.y < nearest.y:
            self.y_delta += 1

        if self.z > nearest.z:
            self.z_delta -= 1
        elif self.z < nearest.z:
            self.z_delta += 1

    def time_step(self):
        self.x += self.x_delta
        self.y += self.y_delta
        self.z += self.z_delta

    def potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def kinetic_energy(self):
        return abs(self.x_delta) + abs(self.y_delta) + abs(self.z_delta)

    def __str__(self):
        return (
            # f'pos=<x={self.x}, y={self.y}, z={self.z}>, '
            # f'vel=<x={self.x_delta}, y={self.y_delta}, z={self.z_delta}>'
            f'pos=<x={str(self.x).rjust(3, " ")}>, '
            f'vel=<x={str(self.x_delta).rjust(3, " ")}>'
        )

    def __repr__(self):
        return self.__str__()


def load_data():
    with open(r'2019\L_12\input.txt') as f:
        return [x.strip('\n') for x in f.readlines()]


def print_moons(moons):
    for moon in moons:
        print(moon, end='|')
    print()


def n_body_problem(data, steps):
    re.compile('')
    moons = []
    for row in data:
        x, y, z = re.findall(r'-?\d+', row)
        moon = Moon(int(x), int(y), int(z))
        moons.append(moon)
    print_moons(moons)

    for step in range(steps):
        new_moons = []
        # print(f"After {step + 1} steps")
        for i in range(len(moons)):
            current_moon = copy(moons[i])
            for j in range(len(moons)):
                nearest_moon = moons[j]
                if i != j:
                    current_moon.add_velocity(nearest_moon)
            new_moons.append(current_moon)
        for moon in new_moons:
            moon.time_step()
        moons = new_moons
        print_moons(moons)
    return sum(
        moon.potential_energy() * moon.kinetic_energy()
        for moon in moons
    )


if __name__ == '__main__':
    data = load_data()
    data = [
        '<x=-1, y=0, z=2>',
        '<x=2, y=-10, z=-7>',
        '<x=4, y=-8, z=8>',
        '<x=3, y=5, z=-1>'
    ]
    # data = [
    #     '<x=-8, y=-10, z=0>',
    #     '<x=5, y=5, z=10>',
    #     '<x=2, y=-7, z=3>',
    #     '<x=9, y=-8, z=-3>'
    # ]
    print(n_body_problem(data, 30))
