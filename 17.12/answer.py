from itertools import product
from collections import defaultdict

def read_data(n):
    with open("data.txt") as f:
        data=defaultdict(int)
        data_list=[list(x) for x in f.read().split("\n")]
        for i in range(len(data_list)):
            for j in range(len(data_list[i])):
                if data_list[i][j]=="#":
                    if n==3:
                        data[(i,j,0)]=1
                    else:
                        data[(i,j,0,0)]=1
    return data

def question(n):
    """
    Работаем в n-мерном пространстве. Если точке соответствует # - то она активна
    Необходимо посчитать количество активных точек после 6 шагов
    Если точка была активна и количество активных соседей рядом с ней равно 2 или 3,
    она остаётся активной
    Если точка не активна и количество рядом активных точек равно 3, то точка точка становится активной
    """
    data=read_data(n)
    for _ in range(6):
        nearest_cubes=defaultdict(int)
        #Считаем количество соседей
        for index, value in data.items():
            if value==1:
                for params in product((-1,0,1), repeat=n):
                    if params==(0,)*n: #Пропускаем текущую точку
                        continue
                    i=tuple([current_index+delta
                             for current_index,delta in zip(index,params)])
                    nearest_cubes[i]+=1
        #Выполняем правило
        wealthy_data= defaultdict(int)
        for index, count in nearest_cubes.items():
            if data[index]==1:
                if 2<=count<=3:
                    wealthy_data[index]=1
            else:
                if count==3:
                    wealthy_data[index]=1
        data=wealthy_data
    print(f"Количество активных фигур {n}-мерном пространстве:", sum(data.values()))
question(3)
question(4)
