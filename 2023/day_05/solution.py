class Action:
    def __init__(self, raw):
        raw_list = raw.split('\n')
        self.name = raw_list[0].split(' ')[0]
        self.intervals = [
            list(map(int, interval.strip(' ').split(' ')))
            for interval in raw_list[1:]
        ]

    def transform(self, seed):
        for destination_start, source_start, length in self.intervals:
            delta = seed - source_start
            if 0 <= delta < length:
                return destination_start + delta
        return seed

    def __str__(self):
        return self.name


def load_data():
    with open(r'2023\day_05\input.txt') as f:
        return f.read()


def seed_to_locaction(data, first=True):
    data_list = data.split('\n\n')
    clear_data_list = [x.strip(' \n') for x in data_list]
    row_seeds = [
        int(seed)
        for seed in clear_data_list[0].split(' ')[1:]
    ]

    actions = []
    for raw_action in clear_data_list[1:]:
        action = Action(raw_action)
        actions.append(action)

    min_result = float('inf')
    if first:
        for seed in row_seeds:
            for action in actions:
                seed = action.transform(seed)
            if seed < min_result:
                min_result = seed
    else:
        for i in range(0, len(row_seeds), 2):
            start = row_seeds[i]
            lenth = row_seeds[i + 1]
            for seed in range(start, start + lenth):
                for action in actions:
                    seed = action.transform(seed)
                    if seed < min_result:
                        min_result = seed
            print(i, len(row_seeds))

    return min_result


if __name__ == '__main__':
    data = load_data()

    # data = '''
    #     seeds: 79 14 55 13

    #     seed-to-soil map:
    #     50 98 2
    #     52 50 48

    #     soil-to-fertilizer map:
    #     0 15 37
    #     37 52 2
    #     39 0 15

    #     fertilizer-to-water map:
    #     49 53 8
    #     0 11 42
    #     42 0 7
    #     57 7 4

    #     water-to-light map:
    #     88 18 7
    #     18 25 70

    #     light-to-temperature map:
    #     45 77 23
    #     81 45 19
    #     68 64 13

    #     temperature-to-humidity map:
    #     0 69 1
    #     1 0 69

    #     humidity-to-location map:
    #     60 56 37
    #     56 93 4
    # '''
    print(seed_to_locaction(data))
    print(seed_to_locaction(data, False))
