def print_array(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j],end="")
        print()
    print("="*20)

def look_at_nearest_cells(data,i,j,simbol):
    """
    Смотрим на ближайшие ячейки и считаем количество
    заполненных элементов указанным символом
    """
    #Внутри
    if ((0<i<len(data)-1) and (0<j<len(data[i])-1)):
        count=0
        if data[i-1][j-1]==simbol: #Левый верхний
            count+=1
        if data[i-1][j]==simbol:   #Верхний
            count+=1
        if data[i-1][j+1]==simbol: #Правый верхний
            count+=1
        if data[i][j-1]==simbol:   #Левый
            count+=1
        if data[i][j+1]==simbol:   #Правый
            count+=1
        if data[i+1][j-1]==simbol: #Левый нижний
            count+=1
        if data[i+1][j]==simbol:   #Нижний
            count+=1
        if data[i+1][j+1]==simbol: #Правый нижний
            count+=1
        return count, 8
    #Левая граница
    if ((0<i<len(data)-1) and (0==j)):
        count=0
        if data[i-1][j]==simbol:   #Верхний
            count+=1
        if data[i-1][j+1]==simbol: #Правый верхний
            count+=1
        if data[i][j+1]==simbol:   #Правый
            count+=1
        if data[i+1][j]==simbol:   #Нижний
            count+=1
        if data[i+1][j+1]==simbol: #Правый нижний
            count+=1
        return count, 5
    #Верхняя граница
    if ((0==i) and (0<j<len(data[i])-1)):
        count=0
        if data[i][j-1]==simbol:   #Левый
            count+=1
        if data[i][j+1]==simbol:   #Правый
            count+=1
        if data[i+1][j-1]==simbol: #Левый нижний
            count+=1
        if data[i+1][j]==simbol:   #Нижний
            count+=1
        if data[i+1][j+1]==simbol: #Правый нижний
            count+=1
        return count, 5
    #Правая граница
    if ((0<i<len(data)-1) and (j==len(data[i])-1)):
        count=0
        if data[i-1][j-1]==simbol: #Левый верхний
            count+=1
        if data[i-1][j]==simbol:   #Верхний
            count+=1
        if data[i][j-1]==simbol:   #Левый
            count+=1
        if data[i+1][j-1]==simbol: #Левый нижний
            count+=1
        if data[i+1][j]==simbol:   #Нижний
            count+=1
        return count, 5
    #Нижняя граница
    if ((i==len(data)-1) and (0<j<len(data[i])-1)):
        count=0
        if data[i-1][j-1]==simbol: #Левый верхний
            count+=1
        if data[i-1][j]==simbol:   #Верхний
            count+=1
        if data[i-1][j+1]==simbol: #Правый верхний
            count+=1
        if data[i][j-1]==simbol:   #Левый
            count+=1
        if data[i][j+1]==simbol:   #Правый
            count+=1
        return count, 5
    #Левый верхний угол
    if ((0==i) and (0==j)):
        count=0
        if data[i][j+1]==simbol:   #Правый
            count+=1
        if data[i+1][j]==simbol:   #Нижний
            count+=1
        if data[i+1][j+1]==simbol: #Правый нижний
            count+=1
        return count, 3
    #Правый верхний угол
    if ((0==i) and (j==len(data[i])-1)):
        count=0
        if data[i][j-1]==simbol:   #Левый
            count+=1
        if data[i+1][j-1]==simbol: #Левый нижний
            count+=1
        if data[i+1][j]==simbol:   #Нижний
            count+=1
        return count, 3
    #Правый нижний
    if ((i==len(data)-1) and (j==len(data[i])-1)):
        count=0
        if data[i-1][j-1]==simbol: #Левый верхний
            count+=1
        if data[i-1][j]==simbol:   #Верхний
            count+=1
        if data[i][j-1]==simbol:   #Левый
            count+=1
        return count, 3
    #Левый нижний
    if ((i==len(data)-1) and (0==j)):
        count=0
        if data[i-1][j]==simbol:   #Верхний
            count+=1
        if data[i-1][j+1]==simbol: #Правый верхний
            count+=1
        if data[i][j+1]==simbol:   #Правый
            count+=1
        return count, 3
    return 0, 0

def look_at_all_vizible_cells(data,i,j,simbol):
    """
    Смотрим на все видимые ячейки и считаем количество
    заполненных элементов указанным символом
    """
    directions=[(0,1),(1,0),(0,-1),(-1,0),
                (1,1),(1,-1),(-1,1),(-1,-1)]
    count=0
    for height_step, width_step in directions:
        current_height=i
        currnet_width=j
        while 0<=(current_height+height_step)<len(data) and 0<=(currnet_width+width_step)<len(data[0]):
            current_height+=height_step
            currnet_width+=width_step

            if data[current_height][currnet_width]=="#":
                count+=1
            if data[current_height][currnet_width]!=".":
                break
    return count

def count_occupied_seats():
    """
    Считаем количество занятых мест
    Если место было пустым (L) и вокруг него нет свободных мест, оно становится занятым
    Если место занято и 4 или больше мест вокруг занято, оно становится пустым
    В других случаях состояние места не меняется
    """
    with open("data.txt") as f:
        raw_data=f.read().split("\n")
        data=[list(row) for row in raw_data]
        for _ in range(100):
            data_after_round=[row.copy() for row in data]
            for i in range(len(data)):
                for j in range(len(data[0])):
                    if data[i][j]=="L":
                        target, all_cells=look_at_nearest_cells(data, i, j,"#")
                        if target==0:
                            data_after_round[i][j]="#"
                    if data[i][j]=="#":
                        target, all_cells=look_at_nearest_cells(data, i, j,"#")
                        if target>=4:
                            data_after_round[i][j]="L"
            data=[row.copy() for row in data_after_round]
        occuped_count=0
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j]=="#":
                    occuped_count+=1
        return occuped_count


def count_occupied_seats_v_2():
    """
    Считаем количество занятых мест
    Если место было пустым (L) и вокруг него по всей длине взгляда
    нет пустых, оно становится занятым
    Если место занято и 5 или больше мест вокруг вдоль взгляда занято,
    оно становится пустым
    В других случаях состояние места не меняется
    """
    with open("data.txt") as f:
        raw_data=f.read().split("\n")
        data=[list(row) for row in raw_data]
        for _ in range(100):
            data_after_round=[row.copy() for row in data]
            for i in range(len(data)):
                for j in range(len(data[0])):
                    if data[i][j]=="L":
                        target=look_at_all_vizible_cells(data, i, j,"#")
                        if target==0:
                            data_after_round[i][j]="#"
                    if data[i][j]=="#":
                        target=look_at_all_vizible_cells(data, i, j,"#")
                        if target>=5:
                            data_after_round[i][j]="L"
            data=[row.copy() for row in data_after_round]

        occuped_count=0
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j]=="#":
                    occuped_count+=1
        return occuped_count

print(count_occupied_seats())
print(count_occupied_seats_v_2())
