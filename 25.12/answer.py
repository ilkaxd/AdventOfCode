def find_loops(start,end):
    """
    Ищем количество циклов шифрования
    """
    value=1
    loops=0
    while value!=end:
        value*=start
        value%=20201227
        loops+=1
    return loops

def encrypt(start,loops):
    """
    Шифруем
    """
    value=1
    for _ in range(loops):
        value*=start
        value%=20201227
    return value

def question():
    """
    Взламываем дверь
    исходное значение = 1
    Затем выполняются несколько циклов:
    - value = value*subject number
    - value = value mod 20201227
    Количество таких циклов заренее неизвестно.

    Криптографическое handshake работает следующим образом:
    - карта преобразует subject number=7 card's secret loop раз.
    В результате получается card's public key
    - дверь преобразует subject number=7 door's secret loop раз.
    В результате получается door's public key
    - карта и дверь используют полученные публичные ключи (исходные данные)
    для обмена, теперь у двери есть card's public key, а у карты
    - карта преобразует card's public key card's secret loop раз.
    Получается encryption key
    - дверь преобразует card's public key door's secret loop раз.
    Получается encryption key, рассчитанный картой
    """
    public_key_card=8987316
    public_key_door=14681524

    loops_card=find_loops(7,public_key_card)
    loops_door=find_loops(7,public_key_door)
    
    print("Encryption key:",encrypt(public_key_card,loops_door))
    #Ну или так, так как сперва если сперва числа вовзести в степень,
    #а потом взять от них остататок аналогично ситуации, когда мы сперва домножаем на
    #это число, а потом находим остаток и всё это циклично
    print(pow(public_key_door, loops_card, 20201227))
    #Это выполняется слишком долго
    #print(public_key_card**loops_door%20201227))

question()
