import re
import sys

sys.setrecursionlimit(100_000)


def load_data():
    with open((r'2021\Q_17\input.txt')) as f:
        return f.readline()


def shot(
    x, y, x_velocity, y_velocity,
    x_min, x_max, y_min, y_max,
    history, i=0
):
    if i > 2_000:
        return None
    if (
        x_min <= x <= x_max
        and
        y_min <= y <= y_max
    ):
        return history

    x += x_velocity
    y += y_velocity
    history.append(y)

    if x_velocity > 0:
        x_velocity -= 1
    elif x_velocity < 0:
        x_velocity += 1
    else:
        pass
    y_velocity -= 1

    return shot(
        x, y,
        x_velocity, y_velocity,
        x_min, x_max,
        y_min, y_max,
        history, i + 1
    )


def trick_shot(data):
    regex = re.compile(r'-?\d+')
    x_min, x_max, y_min, y_max = map(int, regex.findall(data))
    results = []
    for x in range(0, int(x_max * 1.1)):
        for y in range(-200, 200):
            y_history = shot(0, 0, x, y, x_min, x_max, y_min, y_max, [0])
            if y_history is not None:
                results.append(max(y_history))
    return max(results), len(results)


if __name__ == '__main__':
    data = load_data()
    # data = 'target area: x=20..30, y=-10..-5'
    print(trick_shot(data))
