import re


def load_data():
    with open(r'2016\I_09\input.txt') as f:
        return f.readline().strip('\n')


def explosives(row):
    '''
    Имеется строка, в которой мы ищем первое 
    (AxB) - которые выделяет строку размера A
    и повторяет её B раз.
    Если в подстроку входит (XxY), то она рассматривается
    как просто строка. Вычисляется длинна итоговой строки
    '''
    result = ''
    regex = re.compile(r'(\d+.\d+)')
    mo = regex.search(row)
    while mo is not None:
        start_idx = mo.start()
        end_idx = mo.end()

        result += row[:start_idx - 1]

        condition = row[start_idx:end_idx]
        subsequence_len, repeat_count = map(int, condition.split('x'))

        subsequence = row[end_idx + 1:end_idx + subsequence_len + 1]
        subsequence_repeated = subsequence * repeat_count
        result += subsequence_repeated

        new_row = row[end_idx + subsequence_len + 1:]
        row = new_row
        mo = regex.search(row)
        continue

    result += row
    return result


def explosives_2(row):
    '''
    Если в подстроке имеется (XxY) - оно формирует новую подстроку
    размера X, повторяющуюся Y раз
    '''
    result = 0
    regex = re.compile(r'(\d+.\d+)')
    mo = regex.search(row)
    while mo is not None:
        start_idx = mo.start()
        end_idx = mo.end()
        result += len(row[:start_idx - 1])

        condition = row[start_idx:end_idx]
        subsequence_len, repeat_count = map(int, condition.split('x'))
        subsequence = row[end_idx + 1:end_idx + subsequence_len + 1]
        mo = regex.search(subsequence)
        if mo is not None:
            result += explosives_2(subsequence) * repeat_count
        else:
            result += len(subsequence) * repeat_count

        new_row = row[end_idx + subsequence_len + 1:]
        row = new_row
        mo = regex.search(row)
    return result + len(row)


if __name__ == '__main__':
    data = load_data()
    print(len(explosives(data)))
    print(explosives_2(data))
