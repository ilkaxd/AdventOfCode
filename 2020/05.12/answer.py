def find_sit(sequence, row, rule):
    """
    Рекурсивно решаем задачу
    """
    if len(sequence)==1:
        if sequence[0]==rule[0]:
            return row[0]
        else:
            return row[1]
    else:
        if sequence[0]==rule[0]:
            return find_sit(sequence[1:],row[:len(row)//2], rule)
        else:
            return find_sit(sequence[1:],row[len(row)//2:], rule)

def find_max_id():
    """
    Необходимо найти максимальный ID и пропущенный id
    Каждая строка данных представляет собой шифрование,
    аналогичное бинарному поиску
    Первые 7 цифр отвечают за ряд. Они могут принимать F или B:
    которые определяют первую или вторую половину из 128 рядов. Каждая
    буква говорит, в какой половине локальной группы находится место.
    Начинаем со всего ряда и рассматриваем половину от имеющихся мест.
    Если первая буква F, то берём выборку от 0 до 63, а если B, то от
    64 до 127. Последующие буквы сопоставляются ждя половину от указанной
    выборки, пока мы не дойдём до 1 ряда
    Последние 3 за место из 8 возможных мест
    
    """
    with open("data.txt") as f:
        data=f.read().split('\n')
        ids=[]
        for row_column in data:
            row=row_column[:7]
            column=row_column[7:]

            row_list=list(range(128))
            column_list=list(range(8))
            id_row=find_sit(row, row_list,"FB")
            id_column=find_sit(column, column_list,"LR")
            ids.append(id_row*8+id_column)
    ids.sort()
    print(ids)
    for i in range(1,len(ids)-1):
        if (ids[i+1]-ids[i])!=1:
            print("Absent id",ids[i+1])
    print("Min id",min(ids))
    print("Max id",max(ids))

find_max_id()
