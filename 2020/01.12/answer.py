import datetime as dt

def load_data():
    with open("data.txt") as f:
        array=[int(x) for x in f.read().split("\n")]
        return array

def find_2_sum_and_production():
    """
    В Файле data.txt нужно найти 2 числа, которые в сумме дают 2020 и затем перемножить
    эти 2 числа
    """
    array=load_data()
    for i in range(len(array)):
        for j in range(len(array[i:])):
            if (array[i]+array[i+j])==2020:
                return array[i]*array[i+j]

def fast_search_2_sum_and_production():
    array=sorted(load_data())
    first=0
    second=len(array)-1
    while first<second:
        s=array[first]+array[second]
        if s == 2020:
            return array[first]*array[second]
        else:
            if s<2020:
                first+=1
            else:
                second-=1

def find_3_sum_and_production():
    """
    Аналогично, только теперь ищем по 3 цифрам
    """
    with open("data.txt") as f:
        array=[int(x) for x in f.read().split("\n")]
        for i in range(len(array)):
            for j in range(len(array[i:])):
                for k in range(len(array[i+j:])):
                    if (array[i]+array[i+j]+array[i+j+k])==2020:
                        return array[i]*array[i+j]*array[i+j+k]


print(find_2_sum_and_production())

print(fast_search_2_sum_and_production())

print(find_3_sum_and_production())
