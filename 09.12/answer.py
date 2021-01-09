def find_pair(preambla, value):
    for j in range(len(preambla)-1):
        for k in range(j+1,len(preambla)):
            if (preambla[j]+preambla[k])==value:
                return True
    return False
                    
def get_data(max_index):
    with open('data.txt') as f:
        data=f.read().split('\n')
        data=[int(x) for x in data]
        return data[:max_index]

def find_first_bad_number(window_size=25):
    """
    Найти число, которое нельзя получить как сумму из 2
    любых window_size предыдущих чисел
    """
    data=get_data(None)
    for i in range(window_size, len(data)):
        preambla=data[i-window_size:i]
        if not find_pair(preambla, data[i]):
            return data[i], i

    return "Значение не найдено"


def find_contiguous_set(value, max_index):
    """
    Найти посследовательность, которая в сумме даст value
    """
    data=get_data(max_index)
    size=2
    while size<len(data):
        for i in range(size, len(data)):
            preambla=data[i-size:i]
            if sum(preambla)==value:
                return min(preambla)+max(preambla)
        size+=1
    return "Ничего не найдено"

value,max_index=find_first_bad_number()
print(value,max_index)
print(find_contiguous_set(value, max_index))

