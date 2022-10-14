def count_trees_encounter(right, down):
    """
    Считаем количество столкновений с деревьями (#) при движении
    с левого верхнего угла в правый нижний
    Считанный из файла массив может расширяться вправо путём канкатенации
    """
    with open("data.txt") as f:
        array=[x for x in f.read().split("\n")]
        amount=0
        start_index=0
        for i in range(0,len(array),down):
            row=list(array[i])
            if row[start_index]=="#":
                amount+=1
            start_index+=right
            if start_index>=len(row):
                start_index-=len(row)
        return amount

def enumeration():
    """
    Вычисляем сумму столкновений при изменении размеров шагов вправо и вниз
    """
    pairs=[(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    results=[count_trees_encounter(right,down)
             for right,down in pairs]
    result=1
    for x in results:
        result*=x
    return result

print(count_trees_encounter(3,1))
print(enumeration())
