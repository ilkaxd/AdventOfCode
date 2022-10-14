from collections import Counter


def load_data():
    with open(r'2021\H_08\input.txt') as f:
        return [x.rstrip('\n') for x in f.readlines()]


def seven_segment_search(data):
    patterns = {
        '0': (6, []),
        '1': (2, []),
        '2': (5, []),
        '3': (5, []),
        '4': (4, []),
        '5': (5, []),
        '6': (6, []),
        '7': (3, []),
        '8': (7, []),
        '9': (6, [])
    }

    target_patterns = ['1', '4', '7', '8']

    for row in data:
        current_pattern_str, digits_str = row.split(' | ')
        current_pattern = current_pattern_str.split()
        digits = digits_str.split()
        for digit in digits:
            c = Counter(digit)
            keys_count = len(c.keys())
            for target_pattern in target_patterns:
                if patterns[target_pattern][0] == keys_count:
                    patterns[target_pattern][1].append(digit)

    return sum(
        len(patterns[target_pattern][1])
        for target_pattern in target_patterns
    )


if __name__ == '__main__':
    data = load_data()
    # data = [
    #     (
    #         'be cfbegad cbdgef fgaecd cgeb fdcge agebfd '
    #         'fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe'
    #     ),
    #     (
    #         'edbfga begcd cbg gc gcadebf fbgde acbgfd '
    #         'abcde gfcbed gfec | fcgedb cgb dgebacf gc'
    #      ),
    #     (
    #         'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad '
    #         'gfac gcb cdgabef | cg cg fdcagb cbg'
    #     ),
    #     (
    #         'fbegcd cbd adcefb dageb afcb bc aefdc ecdab '
    #         'fgdeca fcdbega | efabcd cedba gadfec cb'
    #     ),
    #     (
    #         'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb '
    #         'dgceab fcbdga | gecf egdcabf bgf bfgea'
    #     ),
    #     (
    #         'fgeab ca afcebg bdacfeg cfaedg gcfdb baec '
    #         'bfadeg bafgc acf | gebdcfa ecba ca fadegcb'
    #     ),
    #     (
    #         'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc '
    #         'dacgb gdcebf gf | cefg dcbef fcge gbcadfe'
    #     ),
    #     (
    #         'bdfegc cbegaf gecbf dfcage bdacg ed bedf '
    #         'ced adcbefg gebcd | ed bcgafe cdgba cbgef'
    #     ),
    #     (
    #         'egadfb cdbfeg cegd fecab cgb gbdefca cg '
    #         'fgcdab egfdb bfceg | gbdfcae bgc cg cgb'
    #     ),
    #     (
    #         'gcafb gcf dcaebfg ecagb gf abcdeg gaef '
    #         'cafbge fdbac fegbdc | fgae cfgab fg bagce'
    #     )
    # ]
    print(seven_segment_search(data))
