from collections import defaultdict

def load_data():
    with open("data.txt") as f:
        data=f.read().split("\n")
    return data

def question():
    """
    Укладываем гексагонную плитку, которая может быть 2 цветов: чёрная и белая
    Изначально все они белой стороной сверху
    В качестве исходных данных дан список пилт, которые следует перевернуть
    Каждая строка - это отдельная плитка, которую нужно перевернуть, при это начиная
    серию шагов, начиная от относительной плитки в центре комнаты
    Каждая плитка имеет 6 соседей: east (e), southeast (se), southwest (sw),
    west (w), northwest (nw), northeast (ne)
    Нужно посчитать сколько останется плиток с чёрной стороной наверху
    """
    data=load_data()
    directions={"e": (1, 0), "se": (0, 1), "sw": (-1, 1),
                "w": (-1, 0), "nw": (0, -1), "ne": (1, -1)}
    state=defaultdict(int) #Белые=0, чёрные=1
    for row in data:
        i,x,y=0,0,0
        while i<len(row):
            letter=row[i]
            if letter in directions:
                dx, dy=directions[letter]
                i += 1
            else:
                dx, dy=directions[row[i:i+2]]
                i+=2
            x,y = x + dx, y+dy
        #Переворачиваем
        if state[(x,y)]==0:
            state[(x,y)]=1
        else:
            state[(x,y)]=0
            
    print("Количество чёрных плит:",sum(v==1 for v in state.values()))
    """
    Добавляем новые правила, которые выполняются каждый день:
    - чёрная плитка с 0 или с более 2 соседних чёрных плиток
    переворачивается на белую сторону
    - белая плитка с 2 чёрными соседними плитками переворачивается на чёрную
    Необходимо посчитать количество чёрных плиток через 100 дней
    """

    for _ in range(100):
        #здесь мы также подхватываем плитки, которые являются белыми, но находятся за пределами основной определённой
        #области, чтобы учесть ситуацию, когда 2 крайние чёрные плитки заставят перевернуться ранее неопределённую 
        keys = set((x + dx, y + dy) for x, y in state.keys() for dx, dy in directions.values())
        new_state=defaultdict(int)
        for x, y in keys: #Проходим по каждой записи
            black_sum=0
            for dx, dy in directions.values():
                black_sum+=state[x+dx, y+dy]
            current=state[x,y]
            if current==1 and (black_sum==0 or black_sum>2):
                new_state[x,y]=0
            elif current==0 and black_sum==2:
                new_state[x,y]=1
            else:
                new_state[x,y]=current
        state=new_state

    print("Количество чёрных плит после 100 дней:",sum(v==1 for v in state.values()))
    
question()
