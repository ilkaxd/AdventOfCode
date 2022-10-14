class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)

    def __str__(self):
        return (
            f'{self.name}: capacity {self.capacity}, '
            f'durability {self.durability}, flavor {self.flavor}, '
            f'texture {self.texture}, calories {self.calories}'
        )

    def __repr__(self):
        return self.__str__()


def load_data():
    with open(r'2015\O_15\input.txt') as f:
        return [x for x in f.read().split('\n') if x != '']


def make_combinations(ingredients, reminded, combination, combinations):
    if len(ingredients) == 1:
        sub_combination = combination.copy()
        sub_combination[ingredients[0].name] = reminded
        combinations.append(sub_combination)
        return
    for i in range(len(ingredients)):
        target_ingredient = ingredients[i]
        reminded_ingredients = ingredients[:i] + ingredients[i + 1:]
        for j in range(reminded + 1):
            sub_combination = combination.copy()
            sub_combination[target_ingredient.name] = j
            make_combinations(
                reminded_ingredients,
                reminded - j,
                sub_combination,
                combinations
            )


def calculate_score(ingredients, combinations):
    result = []
    for combination in combinations:
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        calories = 0
        for ingredient in ingredients:
            count = combination[ingredient.name]
            capacity += count * ingredient.capacity
            durability += count * ingredient.durability
            flavor += count * ingredient.flavor
            texture += count * ingredient.texture
            calories += count * ingredient.calories
        result.append((
            max(0, capacity) *
            max(0, durability) *
            max(0, flavor) *
            max(0, texture),
            calories
        ))
    return result


def best_combination(data, use_caloeries):
    """
    Ищем комбинацию ингредиентов, которая даёт наибольший score
    Ограничение:
        - максимальное количество использований ингредиентов: 100
        - количество калорий равно 500 (для второй задачи)
    """
    ingredients = read_ingrediest(data)
    combinations = []
    make_combinations(
        ingredients,
        100,
        dict((x.name, None) for x in ingredients),
        combinations
    )
    if use_caloeries:
        return max(
            value
            for value, calories in calculate_score(ingredients, combinations)
            if calories == 500
        )
    return max(
        value
        for value, _ in calculate_score(ingredients, combinations)
    )


def read_ingrediest(data):
    ingredients = []
    for row in data:
        (
            name, _,
            capacity, _,
            durability, _,
            flavor, _,
            texture, _,
            calories
        ) = row.split()
        ingredients.append(
            Ingredient(
                name,
                capacity.strip(','),
                durability.strip(','),
                flavor.strip(','),
                texture.strip(','),
                calories
            )
        )
    return ingredients


if __name__ == '__main__':
    data = load_data()
    print(best_combination(data, False))
    print(best_combination(data, True))
