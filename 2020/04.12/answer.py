import re

def count_passwords():
    """
    Считаем количество корректных данных:
    Формат данных
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
    Каждая запись должна быть заполнена. Каждая запись разделяется пустой строкой
    Допускается пропуск cid
    """
    with open("data.txt") as f:
        count=0
        array=[x for x in f.read().split("\n\n")]
        target_fields=['byr','iyr','eyr','hgt','hcl','ecl','pid']
        option_fields=['cid']
        for row in array:
            valid=True
            for target in target_fields:
                if not check_value(fr'{target}:\S+', row)[0]:
                    valid=False
                    break
            if valid:
                count+=1
        return count

def check_value(regex_string, row):
    """
    Проверяем указанное регулярное выражение на указанной строке
    Return: False - если ничего не найдено
    """
    regex=re.compile(regex_string)
    mo=regex.search(row)
    if (mo is None):
        return (False, None)
    return (True, mo.groups())

def count_passwords_strict():
    """
    Считаем количество корректных данных:
    Формат данных
    byr (Birth Year) - 4 цифры с 1920 по 2002
    iyr (Issue Year) - 4 цифры с 2010 по 2020
    eyr (Expiration Year) - 4 цифры с 2020 по 2030
    hgt (Height) - число, после которого идёт:
        - cm - от 150 до 193
        - in - от 59 до 76
    hcl (Hair Color) - знак #, за которым идёт 6 символов 0-9 или a-f 
    ecl (Eye Color) - amb blu brn gry grn hzl oth
    pid (Passport ID) - 9-значное число, начинающееся с 0
    cid (Country ID)
    Каждая запись должна быть заполнена. Каждая запись разделяется пустой строкой
    Допускается пропуск cid
    """
    with open("data.txt") as f:
        count=0
        array=[x for x in f.read().split("\n\n")]
        for row in array:
            #Дата рождения
            condition, value=check_value(r'(byr:\d{4})', row)
            if not condition or not(1920<=int(value[0].split(":")[1])<=2002):
                continue
            
            #Год выпуска
            condition, value=check_value(r'(iyr:\d{4})', row)
            if not condition or not(2010<=int(value[0].split(":")[1])<=2020):
                continue

            #Год окончания
            condition, value=check_value(r'(eyr:\d{4})', row)
            if not condition or not(2020<=int(value[0].split(":")[1])<=2030):
                continue
            
            #Рост
            condition, value=check_value(r'(hgt:\d{2,3})(cm|in)', row)
            if not condition:
                continue
            else:
                height=int(value[0].split(":")[1])
                if value[1]=='cm':
                    if not (150<=height<=193):
                        continue
                elif value[1]=='in':
                    if not (59<=height<=76):
                        continue
                else:
                   continue
            #Цвет волос
            condition, value=check_value(r'(hcl:#)([0-9a-f]{6})', row)
            if not condition and value is None:
                continue
            #Цвет глаз
            condition, value=check_value(r'(ecl:)(amb|blu|brn|gry|grn|hzl|oth)', row)
            if not condition and value is None:
                continue

            #ID паспорта
            condition, value=check_value(r'(pid:)(\d+)', row)
            if not condition and value is None:
                continue
            if  len(value[1])!=9:
                continue
            count+=1
        return count
            
print(count_passwords())
print(count_passwords_strict())
