from collections import defaultdict


class Program:
    def __init__(self, instructions):
        self.registers = defaultdict(int)
        self.instructions = instructions
        self.i = 0
        self.buffer = []
        self.sounds = []
        self.is_blocked = False
        self.send_value_count = 0

    def step(self):
        row = self.instructions[self.i]
        instruction_params = row.split()
        instruction = instruction_params[0]
        params = instruction_params[1:]
        if instruction == 'snd':
            self.send_value_count += 1
            self.sounds.append(self.registers[params[0]])
            self.buffer.append(self.get_value(params[1]))
        elif instruction == 'set':
            self.registers[params[0]] = self.get_value(params[1])
        elif instruction == 'add':
            self.registers[params[0]] += self.get_value(params[1])
        elif instruction == 'mul':
            self.registers[params[0]] *= self.get_value(params[1])
        elif instruction == 'mod':
            self.registers[params[0]] %= self.get_value(params[1])
        elif instruction == 'rcv':
            if self.registers[params[0]] != 0:
                
        elif instruction == 'jgz':
            if self.registers[params[0]] != 0:
                self.i += self.get_value(params[1])
                return
        self.i += 1

    def get_value(self, value):
        if value.lstrip('-').isdigit():
            return int(value)
        return self.registers[value]


def load_data():
    with open(r'2017\R_18\input.txt') as f:
        return [x.strip('\n') for x in f.readlines()]


def duet(data, programs_count=1):
    programs = [Program(data) for _ in range(programs_count)]
    while any(not x.is_blocked for x in programs):
        for x in programs:
            if not x.is_blocked:
                x.step()


if __name__ == '__main__':
    data = load_data()
    # data = [
    #     'set a 1',
    #     'add a 2',
    #     'mul a a',
    #     'mod a 5',
    #     'snd a',
    #     'set a 0',
    #     'rcv a',
    #     'jgz a -1',
    #     'set a 1',
    #     'jgz a -2',
    # ]
    print(duet(data))
