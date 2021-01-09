def load_data():
    with open("data.txt") as f:
        data=f.read().split("\n\n")
        player_1=[int(x) for x in data[0].split("\n")[1:]]
        player_2=[int(x) for x in data[1].split("\n")[1:]]
        return player_1,player_2

def calculate_result(player_1,player_2):
    deck=player_1 if len(player_1)!=0 else player_2
    return sum([card*weight
                for card, weight in zip(deck, list(range(len(deck),0,-1)))])

def question():
    """
    Играем в карточную игру:
    Каждый игрок начинает с одинаковым количеством карт
    На каждом раунде оба игрока берут верхнюю карту и тот, у кого
    значение карты выше, побеждает в раунде. Победитель кладёт обе карты на дно
    своей колоды так, чтобы большая карта лежала выше. Побеждает тот,
    у кого окажутся все карты
    Функция возвращает сумму карт, умноженные на их веса.
    Вес нижней карты 1, вес второй снизу карты 2 и т.д. 
    """
    player_1,player_2=load_data()
    while player_1!=[] and player_2!=[]:
        card_a=player_1.pop(0)
        card_b=player_2.pop(0)

        win_1=False
        if card_a>card_b:
            win_1=True
            player_1=player_1+[card_a,card_b]
        else:
            player_2=player_2+[card_b,card_a]
    
    return calculate_result(player_1,player_2)

print("Сумма произведений =",question())

def game_round(player_1,player_2):
    
    card_a=player_1[0]
    card_b=player_2[0]
    #Запускаем новую подигру
    if card_a<len(player_1) and card_b<len(player_2):
        player_1,player_2=sub_game(player_1[1:card_a+1],player_2[1:card_b+1])
        return bool(player_1)
    else:
        return card_a>card_b

def sub_game(player_1,player_2):
    previous=set() #Сохраняем только уникальные повторения
    while len(player_1)!=0 and len(player_2)!=0:
        
        #бесконечный цикл
        if (player_1,player_2) in previous: 
            return player_1,player_2
        #Сохраняем колоды
        previous.add((player_1,player_2))
        #Победил первый
        if game_round(player_1,player_2):
            player_1,player_2=(player_1[1:]+(player_1[0],player_2[0]),
                               player_2[1:])
        #Победил второй
        else:
            player_1,player_2=(player_1[1:],player_2[1:]+(player_2[0],
                                                          player_1[0]))
    return player_1,player_2
def question_2():
    """
    Рекурсивная версия игры
    Начинаем с теми же картами и каждом шаге выполняем следующие действия:
    - прежде чем каждый игрок достанет карту, если в предыдущем раунде
    игроки имеют те же самые карты в том же самом порядке у тех же игроков,
    игра заканчивается победой 1. Предыдущие раунды других игр не учитываются
    (для предотвращения бесконечной игры)
    - в противном случае, карты этого раунда должны быть заново определены.
    гроки показывают верхнюю карту колоды как обычно
    - если обих игроков остолось карт в колоде меньше чем стоимость карты,
    то победитель определяется в новой рекурсивной игре
    - В противном случае, по крайней мере у одного не должно остаться карт в
    колоде для рекурсии. Победителем раунда становится игрок с более ценной картой
    Для игры в подигру Recursive Combat каждый игрок создаёт новую колоду путём
    копирования следующей карты в их колоде (количество скопированных карт равно
    числу на карте, которую он вытянул)
    """
    player_1,player_2=load_data()
    #Преобразуем в кортеж, чтобы можно подкидывать в set
    player_1,player_2=sub_game(tuple(player_1),tuple(player_2))
    return calculate_result(player_1,player_2)
print("Сумма произведений в рекурсивной игре=",question_2())
