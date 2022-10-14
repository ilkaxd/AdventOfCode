def Intcode(data):
    adds = 1
    multiplies = 2
    halt = 99

    i = 0

    while i < len(data):
        operation = data[i]
        X = data[i + 1]
        Y = data[i + 2]
        Z = data[i + 3]
        if operation == adds:
            data[Z] = data[X] + data[Y]
        elif operation == multiplies:
            data[Z] = data[X] * data[Y]
        elif operation == halt:
            return data[0]
        i += 4
