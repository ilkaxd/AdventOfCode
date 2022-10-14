def read_data():
    with open("data.txt") as f:
        data=f.read().split("\n")
        return data

def rotation(east, north, direction, value):
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    for _ in range(value//90):
        for i in range(len(directions)):
            if (east, north)==directions[i]:
                if direction=="L":
                    east, north=directions[i-1]
                else:
                    if i+1==len(directions):
                        east, north=directions[0]
                    else:
                        east, north=directions[i+1]
                break
    return east, north    

def rotation_axis(east, north, direction, value):
    for _ in range(value//90):
        if direction=="L":
            old_north=north
            north=east
            east=-old_north
        else:
            old_east=east
            east=north
            north=-old_east
    return east, north

def find_manhattan_distance():
    """
    Двигаемся из точки (0,0) в соответствие со списком инструкция:
    Nx - двигаться на North на x клеток
    Sx - двигаться на South на x клеток
    Ex - двигаться на East на x клеток
    Wx - двигаться на West на x клеток
    Lx - сменить направление взгляда на x градусов влево
    Rx - сменить направление взгляда на x градусов вправо
    Fx - двигаться в направлении взгляда на x шагов
    Исходное направление взгляда - East
    """
    data=read_data()
    height=0
    width=0
    north=0
    east=1
    for row in data:
        command=row[0]
        value=int(row[1:])
        if command=="F":
            height+=value*north
            width+=value*east
        elif command=="N":
            height+=value
        elif command=="S":
            height-=value
        elif command=="E":
            width+=value
        elif command=="W":
            width-=value
        elif command=="L" or command=="R":
            east,north=rotation(east,north,command,value)
        else:
            print("Неизвестная команда")
    return abs(height)+abs(width)

def find_relative_manhattan_distance():
    """
    Двигаемся из точки (0,0) в соответствие со списком инструкция:
    Nx - сменить положение относительной точки на x клеток North
    Sx - сменить положение относительной точки на x клеток South
    Ex - сменить положение относительной точки на x клеток East
    Wx - сменить положение относительной точки на x клеток West
    Lx - повернуть плоскость точки на x градусов влево
    Rx - повернуть плоскость точки на x градусов вправо
    Fx - двигаться на x точек вперёд
    Исходное положение точки (east=10, north=1)
    """
    data=read_data()
    height=0
    width=0
    north=1
    east=10
    for row in data:
        start_height=height
        start_width=width
        start_north=north
        start_east=east
        command=row[0]
        value=int(row[1:])
        if command=="F":
            height+=value*north
            width+=value*east
        elif command=="N":
            north+=value
        elif command=="S":
            north-=value
        elif command=="E":
            east+=value
        elif command=="W":
            east-=value
        elif command=="L" or command=="R":
            east,north=rotation_axis(east,north,command,value)
        else:
            print("Неизвестная команда")
    return abs(height)+abs(width)


print(find_manhattan_distance())
print(find_relative_manhattan_distance())
