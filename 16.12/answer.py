def load_data():
    with open("data.txt") as f:
        data=f.read().split("\n\n")
        raw_rules=data[0].split("\n")
        rules={}
        for row in raw_rules:
            param, values=row.split(":")
            left, right=values.split(" or ")
            left=[int(x) for x in left.split("-")]
            right=[int(x) for x in right.split("-")]
            rules[param]=list(range(left[0],left[1]+1))+list(range(right[0],right[1]+1))

        my_ticket=[int(x) for x in data[1].split("\n")[1].split(",")]

        other_tickets_row=[x for x in data[2].split("\n")[1:]]
        other_tickets=[x.split(",") for x in other_tickets_row]
        for i in range(len(other_tickets)):
            for j in range(len(other_tickets[i])):
                other_tickets[i][j]=int(other_tickets[i][j])
        return rules, my_ticket, other_tickets
def error_rate():
    """
    На входе имеем набор правил, значения полей в целевом билете
    и значение полей в группе билетов
    Если поле в билете не подходит ни под одно правило, билет недействительный
    Посчитать сумму недействительных билетов
    После выбрасываем указанные билеты и определяем какой правило соответствует
    какому столбцу
    Затем определяем произведение значений в полях, которые начинаются со слова departure
    """
    error_rate_value=0
    rules, my_ticket, other_tickets=load_data()
    error_rows=[]
    for row in other_tickets:
        for row_value in row:
            able_value=False
            for rule, values in rules.items():
                if row_value in values:
                    able_value=True
                    break
            if able_value==False:
                error_rate_value+=row_value
                error_rows.append(row)
    print("Сумма некорректных полей:",error_rate_value)
    #Удаляем лишние
    for error_row in error_rows:
        other_tickets.remove(error_row)
    #Определяем целевые поля
    all_error_count=[]
    for rule, values in rules.items():
        error_count=[0]*len(other_tickets[0])
        for row in other_tickets:
            for row_index in range(len(row)):
                if row[row_index] not in values:
                    error_count[row_index]+=1
        all_error_count.append([rule, error_count])
    
    all_error_count.sort(key=lambda x: x[1], reverse=True)

    occupied_index=[]
    target_rules=[]
    for error_count in all_error_count:
        target_index=[i for i, v in enumerate(error_count[1])
                      if v == 0 and i not in occupied_index][0]
        occupied_index.append(target_index)
        target_rules.append([error_count[0],target_index])
    target_rules.sort(key=lambda x: x[1])
    result=1
    for rule, index in target_rules:
        if rule.startswith('departure'):
            result*=my_ticket[index]
    print("Прозведение целевых полей:",result)
error_rate()
