class Reindeer:
    def __init__(self, name, speed, duration, rest):
        self.name = name
        self.speed = int(speed)
        self.duration_action = int(duration)
        self.duration_rest = int(rest)
        self.position = 0
        self.available = True
        self.remained_action = int(duration)
        self.remained_rest = 0
        self.score = 0

    def iter(self):
        # fly
        if self.available:
            self.position += self.speed
            self.remained_action -= 1
            if self.remained_action < 1:
                self.remained_action = 0
                self.available = False
                self.remained_rest = self.duration_rest
        # rest
        else:
            self.remained_rest -= 1
            if self.remained_rest < 1:
                self.remained_rest = 0
                self.available = True
                self.remained_action = self.duration_action

    def __str__(self):
        if self.available:
            action = f'move ({self.remained_action} remained)'
        else:
            action = f'rest ({self.remained_rest} remained)'
        return f'{self.name} ({self.position}): {action}'

    def __repr__(self) -> str:
        return self.__str__()


def load_data():
    with open(r'2015\N_14\input.txt') as f:
        return [x for x in f.read().split('\n') if x != '']


def take_parameters(data):
    result = []
    for row in data:
        (
            name, _, _,
            speed, _, _,
            duration, _, _, _, _, _, _,
            rest, _
        ) = row.split()
        result.append(Reindeer(name, speed, duration, rest))
    return result


def reindeer_olympics_2(data, duration):
    """
    Каждую секунду каждый олень зарабатывает очки.
    Если его дистанция максимальная +1, иначе 0
    """
    reindeers = take_parameters(data)
    for _ in range(duration):
        for i in range(len(reindeers)):
            reindeer = reindeers[i]
            reindeer.iter()
        current_max = max(x.position for x in reindeers)
        for i in range(len(reindeers)):
            reindeer = reindeers[i]
            if reindeer.position == current_max:
                reindeer.score += 1
    return max(x.score for x in reindeers)


def reindeer_olympics(data, duration):
    """
    Имеется несколько оленей, у каждого из которых
    есть:
        - скорость
        - время, в течение которого он скачет
        - время отдыха
    нужно найти максимальную дистанцию, которую пробежали
    олени после duration секунд
    """
    reindeers = take_parameters(data)
    for _ in range(duration):
        for i in range(len(reindeers)):
            reindeer = reindeers[i]
            reindeer.iter()
    return max(x.position for x in reindeers)


if __name__ == '__main__':
    data = load_data()
    print(reindeer_olympics(data, 2503))
    print(reindeer_olympics_2(data, 2503))
