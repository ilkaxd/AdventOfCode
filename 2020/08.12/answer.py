def make_operation(index, accum, commands, values, second_invoke):
    #Пришли к концу списка инструкций
    if index>=len(commands):
        return accum
    #Вызываем инструкцию второй раз
    if second_invoke[index]:
        return accum
    second_invoke[index]=True
    operation=commands[index]
    if operation=='nop':
        index+=1
    elif operation=='acc':
        accum+=values[index]
        index+=1
    elif operation=='jmp':
        index+=values[index]
    else:
        print("Неизвестная операция")
    
    return make_operation(index, accum, commands, values, second_invoke)

def gen_data():
    with open('data.txt') as f:
        data=f.read().split('\n')
        commands=[]
        values=[]
        for row in data:
            command,value=row.split(" ")
            commands.append(command)
            values.append(int(value))
        return commands, values

def find_value_in_accumulator(accumulator):
    """
    Выполняем последовательность действий, указанную в файле
    acc x - изменяет значение на указанную величину x
    jmp x - выполняет команду, расположенную на x шагов от текущей точки
    nop x - ничего не делает
    """
    commands, values=gen_data()
        
    #Начинаем с нулевого индекса
    second_invoke=[False]*len(commands)
    accumulator=make_operation(0,accumulator, commands, values, second_invoke)
    return accumulator

def find_corrupted_instruction(accumulator):
    commands, values=gen_data()
    #Просто последовательно меняем
    for i in range(len(commands)):
        accumulator=0
        old=''
        #Меняем
        if commands[i]=='nop':
            old=commands[i]
            commands[i]='jmp'
        elif commands[i]=='jmp':
            old=commands[i]
            commands[i]='nop'
        else:
            continue
        second_invoke=[False]*len(commands)
        accumulator=make_operation(0,accumulator, commands, values, second_invoke)
        if second_invoke[-1]:
            return accumulator
        #Возвращаем
        commands[i]=old
    return "Ошибка не обнаружена"

print(find_value_in_accumulator(0))
print(find_corrupted_instruction(0))
