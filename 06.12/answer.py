from collections import Counter
def sum_of_counts():
    """
    Считаем сколько уникальных значений было в каждой группе и складываем полученные числа
    """
    with open('data.txt') as f:
        count=0
        data=f.read().split('\n\n')
        for group in data:
            concat_row=""
            for row in group.split('\n'):
                concat_row+=row.strip('\n')
            count+=len(set(concat_row))
        return count

def sum_of_everyone_counts():
    """
    Считаем на сколько вопросов внутри группы единоглассно ответили yes и
    складываем полученные числа
    """
    with open('data.txt') as f:
        count=0
        data=f.read().split('\n\n')
        for group in data:
            concat_row=""
            splited_group=group.split('\n')
            for row in splited_group:
                concat_row+=row.strip('\n')
            c=Counter(concat_row)
            for value in c.values():
                if value/len(splited_group)==1:
                    count+=1
        return count
            
print(sum_of_counts())
print(sum_of_everyone_counts())
