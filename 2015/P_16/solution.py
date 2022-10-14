import re

class NewSue:
    def __init__(
        self,
        number=None,
        children=None,
        cats=None,
        samoyeds=None,
        pomeranians=None,
        akitas=None,
        vizslas=None,
        goldfish=None,
        trees=None,
        cars=None,
        perfumes=None
    ):
        self.number = number
        self.children = children
        self.cats = cats
        self.samoyeds = samoyeds
        self.pomeranians = pomeranians
        self.akitas = akitas
        self.vizslas = vizslas
        self.goldfish = goldfish
        self.trees = trees
        self.cars = cars
        self.perfumes = perfumes


class Sue:
    def __init__(
        self,
        number=None,
        children=None,
        cats=None,
        samoyeds=None,
        pomeranians=None,
        akitas=None,
        vizslas=None,
        goldfish=None,
        trees=None,
        cars=None,
        perfumes=None
    ):
        self.number = number
        self.children = children
        self.cats = cats
        self.samoyeds = samoyeds
        self.pomeranians = pomeranians
        self.akitas = akitas
        self.vizslas = vizslas
        self.goldfish = goldfish
        self.trees = trees
        self.cars = cars
        self.perfumes = perfumes

    def __str__(self):
        params = []
        if self.children is not None:
            params.append(f'children: {self.children}')
        if self.cats is not None:
            params.append(f'cats: {self.cats}')
        if self.samoyeds is not None:
            params.append(f'samoyeds: {self.samoyeds}')
        if self.pomeranians is not None:
            params.append(f'pomeranians: {self.pomeranians}')
        if self.akitas is not None:
            params.append(f'akitas: {self.akitas}')
        if self.vizslas is not None:
            params.append(f'vizslas: {self.vizslas}')
        if self.goldfish is not None:
            params.append(f'goldfish: {self.goldfish}')
        if self.trees is not None:
            params.append(f'trees: {self.trees}')
        if self.cars is not None:
            params.append(f'cars: {self.cars}')
        if self.perfumes is not None:
            params.append(f'perfumes: {self.perfumes}')
        params = ', '.join(params)
        return f'Sue {self.number}: {params}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, obj):
        if isinstance(obj, Sue):
            if self.children is not None:
                if self.children != obj.children:
                    return False
            if self.cats is not None:
                if self.cats != obj.cats:
                    return False
            if self.samoyeds is not None:
                if self.samoyeds != obj.samoyeds:
                    return False
            if self.pomeranians is not None:
                if self.pomeranians != obj.pomeranians:
                    return False
            if self.akitas is not None:
                if self.akitas != obj.akitas:
                    return False
            if self.vizslas is not None:
                if self.vizslas != obj.vizslas:
                    return False
            if self.goldfish is not None:
                if self.goldfish != obj.goldfish:
                    return False
            if self.trees is not None:
                if self.trees != obj.trees:
                    return False
            if self.cars is not None:
                if self.cars != obj.cars:
                    return False
            if self.perfumes is not None:
                if self.perfumes != obj.perfumes:
                    return False
            return True
        elif isinstance(obj, NewSue):
            if self.children is not None:
                if self.children != obj.children:
                    return False
            if self.cats is not None:
                if self.cats <= obj.cats:
                    return False
            if self.samoyeds is not None:
                if self.samoyeds != obj.samoyeds:
                    return False
            if self.pomeranians is not None:
                if self.pomeranians >= obj.pomeranians:
                    return False
            if self.akitas is not None:
                if self.akitas != obj.akitas:
                    return False
            if self.vizslas is not None:
                if self.vizslas != obj.vizslas:
                    return False
            if self.goldfish is not None:
                if self.goldfish >= obj.goldfish:
                    return False
            if self.trees is not None:
                if self.trees <= obj.trees:
                    return False
            if self.cars is not None:
                if self.cars != obj.cars:
                    return False
            if self.perfumes is not None:
                if self.perfumes != obj.perfumes:
                    return False
            return True
        return False


def load_data():
    with open(r'2015\P_16\input.txt') as f:
        return [x for x in f.read().split('\n') if x != '']


def check_property(property, query):
    regex = re.compile(rf'{property}: \d+')
    result = regex.findall(query)
    if len(result) > 0:
        value = result[0].split()[1]
        return int(value)
    return None


def analize_sue(data):
    sues = []
    for row in data:
        _, number = row.split()[:2]
        sues.append(
            Sue(
                int(number.strip(':')),
                check_property('children', row),
                check_property('cats', row),
                check_property('samoyeds', row),
                check_property('pomeranians', row),
                check_property('akitas', row),
                check_property('vizslas', row),
                check_property('goldfish', row),
                check_property('trees', row),
                check_property('cars', row),
                check_property('perfumes', row)
            ))
    return sues


def find_sue(
    sues,
    children,
    cats,
    samoyeds,
    pomeranians,
    akitas,
    vizslas,
    goldfish,
    trees,
    cars,
    perfumes,
    task_1=True
):
    """
    Ищем строку, в которой значения совпадают с целевыми
    Если в строке значение не указано, это не значит что оно
    равно нулю
    Для второй задачи:
        - для cats и trees ищем строку, в которой параметры
        меньше указанных
        - для pomeranians и goldfish ищем больше
    """
    if task_1:
        target_sue = Sue(
            'X',
            children,
            cats,
            samoyeds,
            pomeranians,
            akitas,
            vizslas,
            goldfish,
            trees,
            cars,
            perfumes
        )
    else:
        target_sue = NewSue(
            'X',
            children,
            cats,
            samoyeds,
            pomeranians,
            akitas,
            vizslas,
            goldfish,
            trees,
            cars,
            perfumes
        )
    for sue in sues:
        if sue == target_sue:
            return sue.number


if __name__ == '__main__':
    data = load_data()
    children = 3
    cats = 7
    samoyeds = 2
    pomeranians = 3
    akitas = 0
    vizslas = 0
    goldfish = 5
    trees = 3
    cars = 2
    perfumes = 1
    print(
        find_sue(
            analize_sue(data),
            children, cats, samoyeds,
            pomeranians, akitas, vizslas,
            goldfish, trees, cars, perfumes
        ))
    print(
        find_sue(
            analize_sue(data),
            children, cats, samoyeds,
            pomeranians, akitas, vizslas,
            goldfish, trees, cars, perfumes,
            False
        ))
