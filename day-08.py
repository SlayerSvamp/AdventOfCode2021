from functools import cache

test_file = 'data/test/day-08.txt'
data_file = 'data/day-08.txt'

segments_by_digit = [
    'abcefg',
    'cf',
    'acdeg',
    'acdfg',
    'bcdf',
    'abdfg',
    'abdefg',
    'acf',
    'abcdefg',
    'abcdfg',
]

letters = segments_by_digit[8]


def parse(line):
    left, right = line.split(' | ')
    return [
        [*map(set, left.split(' '))],
        right.split(' '),
    ]

@cache
def commons(length):
    common = set(letters)
    for x in segments_by_digit:
        if len(x) == length:
            common &= set(x)
    return common


def get_output(uniques, output):
    possible = {x: set(letters) for x in letters}
    for unique in uniques:
        if len(unique) in (2, 3, 4):
            possible['e'] -= unique

        for segment in commons(len(unique)):
            possible[segment] &= unique

    for value in possible.values():
        for key, to_reduce in possible.items():
            if to_reduce - value:
                possible[key] -= value

    lookup = {''.join(value): key for key, value in possible.items()}
    res = ''
    for digit in output:
        code = ''.join(sorted(lookup[x] for x in digit))
        res += str(segments_by_digit.index(code))

    return int(res)


def process(file):
    lines = [*map(parse, open(file).read().splitlines())]
    part_1 = sum(len(x) in [2, 3, 4, 7] for _, output in lines for x in output)
    part_2 = sum(get_output(*line) for line in lines)

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 26, p1t
assert p2t == 61229, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
