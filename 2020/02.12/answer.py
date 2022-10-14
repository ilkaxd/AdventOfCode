import re

def count_right_passwords():
    """
    Необходимо посчитать сколько паролей удовлетворяют описанной политике:
    политика описывается слева от пароля и имеет формат:
    {min amount X}-{max amount X} : X
    где
    - min amount X - минимальное количество вхождений литеры X
    - min amount X - максимальное количество вхождений литеры X
    - X - исследуемая буква
    """
    with open("data.txt") as f:
        array=[x for x in f.read().split("\n")]
        amount=0
        for row in array:
            policy, password=row.split(":")
            min_max_count, letter=policy.split(" ")
            min_count, max_count=min_max_count.split("-")
            regex_condition=f"({letter})"
            regex=re.compile(regex_condition)
            mo=regex.findall(password)
            if int(min_count)<=len(mo)<=int(max_count):
                amount+=1
        return amount

def count_right_passwords_2():
    """
    Необходимо посчитать сколько паролей удовлетворяют описанной политике:
    политика описывается слева от пароля и имеет формат:
    {min amount X}-{max amount X} : X
    где
    - min amount X - позиция, в которой должна быть литера X
    - min amount X - позиция, в которой не должно быть литеры X
    - X - исследуемая буква
    Отсчёт начинается с 1
    """
    with open("data.txt") as f:
        array=[x for x in f.read().split("\n")]
        amount=0
        for row in array:
            policy, password=row.split(":")
            password=password.strip(" ")
            min_max_count, letter=policy.split(" ")
            min_count, max_count=min_max_count.split("-")
            first=password[int(min_count)-1]==letter
            second=password[int(max_count)-1]==letter
            if (first or second) and (first!=second):
                amount+=1
        return amount

print(count_right_passwords())
print(count_right_passwords_2())
