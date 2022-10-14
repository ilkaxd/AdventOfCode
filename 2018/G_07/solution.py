import re
import string


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []
        self.visited = False

    def __str__(self):
        return f'{self.name} -> ({[node.name for node in self.children]})'

    def __repr__(self) -> str:
        return f'{self.name} -> ({[node.name for node in self.children]})'

    def is_available(self):
        return all(node.visited for node in self.parents)


class Worker:
    def __init__(self, delay=60):
        self.task = None
        self.is_available = True
        self.rest_work_time = 0
        self.delay = delay

    def iteration(self):
        if self.is_available:
            return []
        self.rest_work_time -= 1
        if self.rest_work_time == 0:
            self.is_available = True
            children = sorted(
                self.task.children,
                key=lambda x: x.name
            )
            self.task = None
            return children
        return []

    def add_task(self, task):
        self.task = task
        chrs = string.ascii_uppercase
        self.is_available = False
        self.rest_work_time = chrs.index(task.name) + self.delay + 1

    def __str__(self):
        if self.is_available:
            return 'Работник свободен'
        else:
            return (
                f'Работник занят задачей {self.task.name} '
                f'(осталось {self.rest_work_time} сек)'
            )

    def __repr__(self):
        return self.__str__()


def load_data():
    with open(r'2018\G_07\input.txt') as f:
        return f.readlines()


def get_node(nodes, name):
    for node in nodes:
        if node.name == name:
            return node
    node = Node(name)
    nodes.append(node)
    return node


def get_nodes(steps):
    regex = re.compile(
        r'Step (\w) must be finished before step (\w) can begin'
    )

    nodes = []

    for step in steps:
        result = regex.search(step)
        head = result.group(1)
        child = result.group(2)
        head_node = get_node(nodes, head)
        child_node = get_node(nodes, child)
        head_node.children.append(child_node)
        child_node.parents.append(head_node)
    available_nodes = [node for node in nodes if node.parents == []]
    return sorted(available_nodes, key=lambda x: x.name)


def InstructionSteps(steps):
    available_nodes = get_nodes(steps)
    result = ''

    while available_nodes != []:
        node = available_nodes.pop(0)
        if not node.visited:
            if not node.is_available():
                available_nodes.append(node)
            else:
                result += node.name
                available_nodes += node.children
                available_nodes = sorted(available_nodes, key=lambda x: x.name)
                node.visited = True
    return result


def InstructionSteps2(steps, worker_counts):
    available_nodes = get_nodes(steps)
    result = ''
    workers = [Worker() for _ in range(worker_counts)]
    i = 0
    while (
        available_nodes != []
        or
        any(not worker.is_available for worker in workers)
    ):
        for _ in range(len(available_nodes)):
            if any(worker.is_available for worker in workers):
                node = available_nodes.pop(0)
                for worker in workers:
                    if worker.is_available:
                        worker.add_task(node)
                        node.visited = True
                        break
        for worker in workers:
            for task in worker.iteration():
                if not task.visited:
                    available_nodes.append(task)
        i += 1
    return i


if __name__ == '__main__':
    data = load_data()
    # data = [
    #     'Step C must be finished before step A can begin.',
    #     'Step C must be finished before step F can begin.',
    #     'Step A must be finished before step B can begin.',
    #     'Step A must be finished before step D can begin.',
    #     'Step B must be finished before step E can begin.',
    #     'Step D must be finished before step E can begin.',
    #     'Step F must be finished before step E can begin.',
    # ]
    # print(InstructionSteps(data))
    print(InstructionSteps2(data, 5))
