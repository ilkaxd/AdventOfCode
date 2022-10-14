def load_data():
    """
    Формированиия графа это длительный процесс, поэтому используем сериализацию
    """
    with open("data.txt") as f:
        data=f.read().split("\n")
    return sorted([int(x) for x in data])  

def find_adapter_chain():
    """
    Необходимо найти максимально длинную последовательность адаптеров,
    разница между каждым из которых не может быть больше 3 и вернуть
    произведение количества адаптеров с разницей 1 и 3
    """
    data=load_data()

    adapter_1=0
    adapter_3=0
    volt=0
    
    for adapter in data:
        delta=adapter-volt

        if delta==1:
            adapter_1+=1
        if delta==3:
            adapter_3+=1
        volt+=delta
    adapter_3+=1
    return adapter_1*adapter_3

def chain_count():
    """
    Считаем количество возможных комбинаций
    """
    data=load_data()
    parents=[0]*(data[-1]+1)
    parents[0]=1
    for n in data:
        child=parents[:n][-3:]
        parents[n]=sum(child)
    return parents[-1]


print(find_adapter_chain())
print(chain_count())
