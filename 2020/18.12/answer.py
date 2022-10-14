import re

def inner_calculate(equation, precedence):
    equation=equation.split()
    if precedence:
        while "+" in equation:
            p_index=equation.index("+")
            equation[p_index-1]=int(equation[p_index-1])+int(equation[p_index+1])
            del equation[p_index:p_index+2]
    
    result=int(equation[0])
    operation=""
    for letter in equation[1:]:
        if str(letter).isdigit():
            if operation=="+":
                result+=int(letter)
            if operation=="*":
                result*=int(letter)
        if letter!=" ":
            operation=letter
    return result

def calculate(equation, precedence):
    regex=re.compile(r'\([\d +*]+?\)')
    while not isinstance(equation,int):
        mo=regex.findall(equation)
        if mo==[]:
            equation=inner_calculate(equation, precedence)
        for m in mo:
            if m.count("(")==1 and m.count(")")==1:
                value=inner_calculate(m.strip("()"), precedence) #Откидываем скобки
                equation=equation.replace(m, str(value))
    return equation
            
def question(precedence):
    """
    Вычисляем уравнения.
    1) Операции + и * имеют одинаковый приоритет и выполняются слева направо
    1) Операции + выше *
    """
    
    with open("data.txt") as f:
        data=f.read().split("\n")
        result=0
        for row in data:
            result+=calculate(row, precedence)
        return result

#print("Сумма без учёта приоритета операций:",question(False))
print("Сумма с с приоритета операций:",question(True))
