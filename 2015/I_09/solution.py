class City:
    def __init__(self, name):
        self.name = name
        self.neighbours = {}

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        return self.name == other.name

    def __str__(self):
        neighbors_names = ', '.join([
            f"{neighbour} ({distance})"
            for neighbour, distance in self.neighbours.items()
        ])
        return f'{self.name}: {neighbors_names}'

    def __repr__(self):
        neighbors_names = ', '.join([
            f"{neighbour} ({distance})"
            for neighbour, distance in self.neighbours.items()
        ])
        return f'{self.name}: {neighbors_names}'


def load_data():
    with open(r'2015\I_09\input.txt') as f:
        return [x for x in f.read().split('\n') if x != '']


def BuildGraph(data):
    cities = []
    for row in data:
        X, _, Y, _, distance = row.split()
        cities.append(X)
        cities.append(Y)
    cities = list(set(cities))
    for i in range(len(cities)):
        cities[i] = City(cities[i])

    for row in data:
        X, _, Y, _, distance = row.split()
        distance = int(distance)
        cities[cities.index(X)].neighbours[Y] = distance
        cities[cities.index(Y)].neighbours[X] = distance
    return cities


def FindDistance(position, visited, result, distances, cities):
    if all(visited.values()):
        distances.append(result)
        return
    for neighbour_name, distance in position.neighbours.items():
        if not visited[neighbour_name]:
            leaf = visited.copy()
            leaf[neighbour_name] = True
            leaf_position = [x for x in cities if x.name == neighbour_name][0]
            FindDistance(
                leaf_position, leaf, result + distance, distances, cities
            )


def FindTargetDistance(data, min_find=True):
    """
    Решаем задачу о коммивояжере
    """
    cities = BuildGraph(data)
    distances = []

    for city in cities:
        visited = dict((city.name, False) for city in cities)
        visited[city.name] = True
        FindDistance(city, visited, 0, distances, cities)
    if min_find:
        return min(distances)
    return max(distances)


if __name__ == '__main__':
    data = load_data()
    print(FindTargetDistance(data))
    print(FindTargetDistance(data, False))
