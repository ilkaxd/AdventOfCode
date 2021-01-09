from itertools import product

def make_sequences(index, rules):
    values=rules[index]
    if isinstance(values,str):
        yield values
    else:
        for rule in values:         #Проходим по |
            for sequences in product(*[make_sequences(value, rules) for value in rule]): #Проходим по единому списку и генерируем возможные комбинации пар
                yield "".join(sequences)
    
def question():
    with open("data.txt") as f:
        rules={}
        row_rules, records=f.read().split("\n\n")
        records=records.split("\n")
        row_rules=row_rules.split("\n")
        for rule in row_rules:
            index,values=rule.split(":")
            values=values.split("|")
            values=[x.strip().split(" ") for x in values]
            is_alpha=False
            for i in range(len(values)):
                for j in range(len(values[i])):
                    if values[i][j].isdigit():
                        values[i][j]=int(values[i][j])
                    else:
                        is_alpha=True
                        values[i][j]=values[i][j].strip("\"")
            if is_alpha:
                rules[int(index)]=values[0][0]
            else:
                rules[int(index)]=values

        #генерируем допустимые последовательности
        available_records=set(make_sequences(0, rules))
        
        #Проверяем имеющиеся записи
        print("Количество допустимых записей:", sum(record in available_records
                                                    for record in records))

        #Устраняем ошибку, которая приводит к появлению петель в графе
        #rules[8]=[[42],[42,8]]
        #rules[11]=[[42, 31],[42, 11, 31]]
        
        
        first_rule=set(make_sequences(42, rules))
        second_rule=set(make_sequences(31, rules))
        step = min([len(x) for x in first_rule]) #шаг проверки
        
        available_records_count=0
        #проверяем чтобы все участки текста были корректными
        for record in records:
            first_include = [record[i:i+step] in first_rule for i in range(0, len(record), step)]
            second_include = [record[i:i+step] in second_rule for i in range(0, len(record), step)]
            if any(all(first_include[:i]) and all(second_include[i:]) and i > (len(first_include) - i) for i in range(len(first_include))):
                available_records_count += 1
    
        print("Количество допустимых записей после обновления:", available_records_count)
        
question()
