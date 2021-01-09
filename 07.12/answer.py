import re

def find_upper_color(current_color, all_colors):
    related_colors=[]
    for master, slaves in all_colors.items():
        if current_color in slaves:
            if master not in related_colors:
                related_colors.append(master)
    finded_colors=[]
    for color in related_colors:
        finded_colors+=find_upper_color(color, all_colors)
    related_colors+=finded_colors
    return related_colors

def count_bags(current_color, all_colors):
    count=0
    investigated_bags=all_colors[current_color]
    for bag in investigated_bags:
        bags_count=int(bag[0])
        inner_count=bags_count+bags_count*count_bags(bag[1],all_colors)
        count+=inner_count
    return count

def parse_rows(regex):
    colors_relation={}
    with open("data.txt") as f:
        data=f.read().split('\n')
        regex=re.compile(regex)
        for row in data:
            master, slave=row.split(" contain ")
            master=master[:-5]  #Отбросили слово bags
            slave=slave[:-1]    #Отбросили точку
            slave_colors=[]
            for color in slave.split(','):
                color=regex.findall(color)
                if color==[]:
                    continue
                slave_colors.append(color[0])
            colors_relation[master]=slave_colors
    return colors_relation

def count_bag_colors(target_color):
    """
    Считаем сколько цветов напрямую или через промежуточные цвета связаны
    с целевым цветом
    """
    colors_relation=parse_rows("\d (.*) bag")
    colors=find_upper_color(target_color, colors_relation)
    print("Количество уникальных цветов:",len(set(colors)))

def count_inner_bags(target_color):
    """
    Считаем количество вложенных сумок
    """
    colors_relation=parse_rows("(\d) (.*) bag")
    count=count_bags(target_color, colors_relation)
    print("Количество вложенных сумок:",count)
count_bag_colors("shiny gold")
count_inner_bags("shiny gold")
