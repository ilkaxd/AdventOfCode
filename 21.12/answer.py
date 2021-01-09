def count_safe_products():
    """
    Исходный набор данных представляет собой список из ингредиентов и
    аллергнов, которые встречаются среди этих ингредиентов
    Необходимо посчитать сколько раз встречаются ингредиенты, которые
    не приводят к аллергии
    """
    with open("data.txt") as f:
        raw_data=f.read().split("\n")
        all_allergens={}
        data=[]
        for row in raw_data:
            ingredients, allergens= row.split(" (contains ")
            ingredients=set(ingredients.split(" "))
            allergens=allergens[:-1].split(", ")

            #Сохраняем в общий список
            for allergen in allergens:
                if allergen not in all_allergens.keys():
                    all_allergens[allergen]=set(ingredients)             
                else:
                    all_allergens[allergen]=set.intersection(all_allergens[allergen],
                                                             set(ingredients))
            data.append((ingredients,allergens))

        allergen_ingredients=set()
        for ingredient in all_allergens.values():
            allergen_ingredients=set.union(allergen_ingredients,ingredient)

        safety_ingredients=[]
        for ingredients, _ in data:
            for ingredient in ingredients:
                if ingredient not in allergen_ingredients:
                    safety_ingredients.append(ingredient)
        print("Сколько раз в списке встречаются безопасные ингредиенты?",
              len(safety_ingredients))

        """
        Теперь определяем какие ингредиенты содержат какие алергены
        Сортируем полученный список ингредиентов в алфавитном порядке
        по именам алергенов
        """
        allergen_ingredients=list(allergen_ingredients)
        sorted_allergens= sorted(list(all_allergens.keys()))
        graph=[[] for _ in allergen_ingredients]
        for allergen, ingredients in all_allergens.items():
            #print(allergen, ingredients)
            for ingredient in ingredients:
                graph[sorted_allergens.index(allergen)].append(ingredient)

        #По имеющемуся списку нужно пройтись и определить какой чему соответствует
        identified=[]
        """
        Да, да, если бы у нас не было бы треугольной системы уравненний
        (не было бы ингредиента, который бы явно соответствовал бы 1 алергену
        и это всё идёт дальше по цепочке), а были бы классические системы уравнений,
        где n=m, то я бы всё равно её приводил бы к треуголному и решал бы через Гаусса
        """
        for _ in range(len(graph)+1):
            for i in range(len(graph)):
                if len(graph[i])==1:
                    identified.append(graph[i][0])
                else:
                    result=[]
                    for j in range(len(graph[i])):
                        if graph[i][j] not in identified:
                            result.append(graph[i][j])
                    graph[i]=result

        result=",".join([x[0] for x in graph])
        print("Целеваяя последовательность:",result)
        
count_safe_products()
