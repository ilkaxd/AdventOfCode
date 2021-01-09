import datetime as dt
def print_cups(array, current_cup):
    for cup in array:
        if cup==current_cup:
            print(f"({cup})", end=" ")
        else:
            print(cup, end=" ")
    print()

#Под запись хэш-таблицы
class Cup():
    def __init__(self, label):
        self.label=label
        self.next_cup=None
    def __str__(self):
        return "(%s, %s)"%(self.label, self.next_cup)         

def question(sequence, N,vizualization=True):
    """
    Имеется 5 цифр, расположенных по кругу по часовой стрелке.
    Сперва определяется первое число в списке как current cup
    Затем осуещствляется 100 шагов, которые сопроваждаются следующими действиями:
        - из списка забираются 3 cups от current cup, а пропуски заполняются, чтобы
        поддерживать круг
        - выбирается destination cup - это cup, метка которой=current cup-1. Вычитание
        идёт до тех пор, пока не будет найдена cup с указанной меткой. Если разница
        стала меньше наименьшей метки, выбирается cup с наибольшей меткой
        - возвращаются убранные 3 cups и вставляются за destination cup
        - выбирается следующая current cup
    """
    for i in range(N):        
        #Забираем 3 cup
        pick_up=sequence[1:4]

        #Ищем целевую cup
        destination_cup=sequence[0]-1 if sequence[0]>min(sequence) else max(sequence)
        while destination_cup in pick_up:
            destination_cup-=1
            if destination_cup<min(sequence):
                destination_cup=max(sequence)

        if (vizualization):
            print(f"-- move {i+1}--")
            print_cups(sequence, sequence[i%len(sequence)])
            print("pick up:", pick_up)
            print("destination:",destination_cup)
            print()
            
        #Возвращаем 3 cup
        insert_index=sequence.index(destination_cup)+1
        if insert_index!=1:
            sequence=[sequence[0]]+sequence[4:insert_index]+pick_up+sequence[insert_index:]
        #Прокручиваем правильным образом
        sequence=sequence[1:]+[sequence[0]]
    
    index=sequence.index(1)
    sequence=sequence[index:]+sequence[:index]
    return sequence[1:]

def question_2(sequence,N):
    cups={}
    len_sequence=len(sequence)
    #Создаём список под все чашки
    for i in range(1, len_sequence+1):
        cups[i]=Cup(i)
        
    #Создаём связанные элементы
    for current_label, next_label in zip(sequence, sequence[1:]):
        cups[current_label].next_cup=cups[next_label]
        
    #Последний элемент ссылается на первый
    cups[len_sequence].next_cup=cups[sequence[0]] 
    start_cup=cups[sequence[0]]
    
    for i in range(N):
        #Забираем 3 cup
        pick_up_start=start_cup.next_cup
        pick_up_middle=pick_up_start.next_cup
        pick_up_end=pick_up_middle.next_cup
        pick_up_labels=[pick_up_start.label,
                        pick_up_middle.label,
                        pick_up_end.label]

        #Ищем целевую cup
        destination_cup=start_cup.label - 1 if start_cup.label>1 else len_sequence
        while destination_cup in pick_up_labels:
            destination_cup-=1
            if destination_cup==0:
                destination_cup=N

        #Возвращаем 3 cup
        start_cup.next_cup=pick_up_end.next_cup
        pick_up_end.next_cup=cups[destination_cup].next_cup
        cups[destination_cup].next_cup=pick_up_start

        #Смещаемся правее
        start_cup=start_cup.next_cup

    after_1=cups[1].next_cup
    next_after_1=cups[1].next_cup.next_cup
    return (after_1.label, next_after_1.label)
    
sequence=[7,9,2,8,4,5,1,3,6]
result=question(sequence, 100, False)
print("Метки после cup 1 в конце 100 шага:","".join(str(x) for x in result))
"""
Теперь имеются 1_000_000 cups, которые после 9 нумеруются в возрастающем порядке
и необходимо совершить 10_000_000 таких шагов, после чего необходимо найти
точки слева и справа от метки 1 перемножить их. Предыдущий подход не подходит,
так как скорость расчёта для такого случая составляет 10 циклов в секунду (при 1e6 параметров)
для массива. Для наших целей подойдёт лучше подойдёт связанный кеш-таблица
"""
sequence+=list(range(len(sequence)+1,int(1e6)+1))
start=dt.datetime.now()
result=question_2(sequence, int(10e6))
print("Произведение меток, которые идут после чашки 1:", result[0]*result[1])
print("Время выпонения программы",dt.datetime.now()-start)
