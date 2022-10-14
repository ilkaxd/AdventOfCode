import re
from datetime import datetime, timedelta

from collections import Counter

class Guard:
    def __init__(self, idx):
        self.idx = idx
        self.sleep_timesteps = []
        self.is_sleep = False
        self.falls_asleep_timestamp = None

    def falling_asleep(self, timestamp):
        self.is_sleep = True
        self.falls_asleep_timestamp = timestamp

    def wake_up(self, timestamp):
        self.is_sleep = False
        delta = (timestamp - self.falls_asleep_timestamp).seconds // 60
        self.sleep_timesteps += [
            self.falls_asleep_timestamp + timedelta(minutes=x)
            for x in range(delta)
        ]

    def minutes_asleep(self):
        return len(self.sleep_timesteps)

    def __str__(self):
        return f'Guard {self.idx}'


def load_data():
    with open(r'2018\D_04\input.txt') as f:
        return [x for x in f.read().split('\n') if x != '']


def sort_rows(data):
    result = []
    regex = re.compile(r'\[(.+)\]')
    for x in data:
        timestamp = datetime.strptime(
            regex.search(x).group(1),
            '%Y-%m-%d %H:%M'
        )
        action = x[19:]
        result.append([timestamp, action])
    return sorted(result, key=lambda x: x[0])


def get_key_by_value(dictionary, target):
    for key, value in dictionary.items():
        if value == target:
            return key
    return -1


def repose_record(data):
    timestamp_action = sort_rows(data)

    guards = {}
    current_guard = None
    regex = re.compile(r'Guard #(\d+)')
    for timestamp, action in timestamp_action:
        guard = regex.search(action)
        if guard is not None:
            idx = int(guard.group(1))
            current_guard = guards.get(idx)
            if current_guard is None:
                current_guard = Guard(idx)
            guards[idx] = current_guard
        else:
            if action == 'wakes up':
                current_guard.wake_up(timestamp)
            elif action == 'falls asleep':
                current_guard.falling_asleep(timestamp)
            else:
                print(f'Ошибочное действие {action}')
    most_asleep_guard = max(
        guards.values(),
        key=lambda x: x.minutes_asleep()
    )

    results = {}
    for idx, guard in guards.items():
        if guard.sleep_timesteps != []:
            minute = Counter(
                x.minute for x in guard.sleep_timesteps
            ).most_common(1)[0]
            results[idx] = minute

    most_frequency_minute = max(
        results.values(),
        key=lambda x: x[1]
    )

    return (
        most_asleep_guard.idx * results[most_asleep_guard.idx][0],
        get_key_by_value(
            results,
            most_frequency_minute
        ) * most_frequency_minute[0]
    )


if __name__ == '__main__':
    data = load_data()
    data = [
        '[1518-11-01 00:00] Guard #10 begins shift',
        '[1518-11-01 00:05] falls asleep',
        '[1518-11-01 00:25] wakes up',
        '[1518-11-01 00:30] falls asleep',
        '[1518-11-01 00:55] wakes up',
        '[1518-11-01 23:58] Guard #99 begins shift',
        '[1518-11-02 00:40] falls asleep',
        '[1518-11-02 00:50] wakes up',
        '[1518-11-03 00:05] Guard #10 begins shift',
        '[1518-11-03 00:24] falls asleep',
        '[1518-11-03 00:29] wakes up',
        '[1518-11-04 00:02] Guard #99 begins shift',
        '[1518-11-04 00:36] falls asleep',
        '[1518-11-04 00:46] wakes up',
        '[1518-11-05 00:03] Guard #99 begins shift',
        '[1518-11-05 00:45] falls asleep',
        '[1518-11-05 00:55] wakes up',
    ]
    print(repose_record(data))
