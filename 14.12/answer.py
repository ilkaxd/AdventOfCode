import re
from itertools import product

def use_mask(value, mask):
    """
    Используется битовая маска:
    X в маске копирует входный бит в выход
    в противном случае бит заменяется значением из маски
    """
    bins=bin(value)[2:].rjust(36,"0") #Преобразуем в биты и дополняем слева
    transformed=""
    for i in range(len(bins)):        #Используем маску
        if mask[i]=="X":
            transformed+=bins[i]
        else:
            transformed+=mask[i]
    return int("0b"+transformed,2)    #Из бит в число

def use_mask_to_index(index, mask):
    """
    Используется битовая маска:
    0 - не изменяет входного бита
    1 - меняет его на 1
    X - допускает использование и 0 и 1
    """
    bins=bin(index)[2:].rjust(36,"0") #Преобразуем в биты и дополняем слева
    transformed=""
    repeat=0
    for i in range(len(bins)):        #Используем маску
        if mask[i]=="0":
            transformed+=bins[i]
        elif mask[i]=="1":
            transformed+="1"
        else:
            transformed+="X"
            repeat+=1
    if repeat==0:
        return [int("0b"+transformed,2)]
    else:
        results=[]
        for params in product(("0","1"),repeat=repeat):
            new_index=""
            j=0
            for i in range(len(transformed)):
                if transformed[i]!="X":
                    new_index+=transformed[i]
                else:
                    new_index+=params[j]
                    j+=1
            results.append(int("0b"+new_index,2))
        return results   #Из бит в число

def use_mask_and_find_sum():
    """
    Накладываем маску на значения и считаем сумму всех значений словаря
    """
    with open("data.txt") as f:
        data=f.read().split("\n")

        mask=""
        results={}
        regex=re.compile(r"\[\d+\]")
        for row in data:
            if row.startswith("mask"):
                mask=row.split("=")[1].strip()
                continue
            if row.startswith("mem"):
                index=int(regex.search(row).group()[1:-1])
                value=int(row.split("=")[1].strip())
                results[index]=use_mask(value, mask)
    return sum(results.values())

def use_mask_with_floating():
    """
    Накладываем маску на индексы и считаем сумму всех значений словаря
    """
    with open("data.txt") as f:
        data=f.read().split("\n")

        mask=""
        results={}
        regex=re.compile(r"\[\d+\]")
        for row in data:
            if row.startswith("mask"):
                mask=row.split("=")[1].strip()
                continue
            if row.startswith("mem"):
                index=int(regex.search(row).group()[1:-1])
                value=int(row.split("=")[1].strip())
                for transformed_index in use_mask_to_index(index, mask):
                    results[transformed_index]=value                
        return sum(results.values())
print(use_mask_and_find_sum())
print(use_mask_with_floating())
