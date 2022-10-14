def gcd_advanced(a,b):
    """
    Модифицированный алгоритм Евклида для получения уравнения вила:
    ax+by=gcd⁡(a,b)
    """
    if b==0:
        return (1,0,a)
    x,y,g=gcd_advanced(b,a%b)
    return (y,x-(a//b)*y,g)

def get_key(dictionary, v):
    for key, value in dictionary.items():
        if value==v:
            return key
def load_data():
    with open("data.txt") as f:
        data=f.read().split("\n")
        timestamp=int(data[0])
        splited_data=data[1].split(',')
        buses=[]
        delta=[]
        for i in range(len(splited_data)):
            x=splited_data[i]
            if x.isdecimal():
                buses.append(int(x))
                delta.append(int(x)-i)
        return timestamp, buses,delta
def find_early_bus():
    """
    Находим автобус, который приедет к указанной временной точке максимально быстро
    """
    timestamp, buses, _=load_data()
    schedule={}
    for bus in buses:
        schedule[bus]=bus-timestamp%bus
    min_wait=min(schedule.values())
    target_bus=get_key(schedule, min_wait)
    return target_bus*min_wait

def find_early_timestamp():
    """
    Найти временную точку из уравнений вида:
    delta[0]=x mod buses[0]
    delta[1]=x mod buses[1]
    ...
    delta[n]=x mod buses[n]

    Что соответствует китайской теореме об остатках,
    решаемой через расширенный алгоритм Евклида:
    1) Вычисляем M=Произведение всех интервалов движения автобусов
    2) Находим все Mi=M/a_i, где a_i=интервал движения конкретного автобуса
    3) Находим Mi^(-1)=1/Mi mod a_i через расширенный алгоритм евклида
    4) Вычисляем искомое значение x=sum(delta[i]MiMi^(-1)) mod M

    Чтобы обойти проблему, связанную с ситуацией, когда остаток больше делителя
    будем вычислять delta симметрично относительно buses[0] со смещением на фактическое delta
    """
    _, buses, delta=load_data()
    array_len=len(buses)
    
    M=1
    for i in range(array_len):
        M*=buses[i]
    M_i=[]
    for i in range(array_len):
        M_i.append(M//buses[i])
    M_i_m1=[]
    
    for i in range(array_len):
        x,y,gcd=gcd_advanced(M_i[i],buses[i])
        M_i_m1.append(x+buses[i])
    result=0
    for i in range(array_len):
        result+=delta[i]*M_i[i]*M_i_m1[i]
    result=result%M
    test=[]
    for i in range(array_len):
        test.append(result%buses[i])

    return result

print(find_early_bus())
print(find_early_timestamp())
