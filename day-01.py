test_file = 'data/test/day-01.txt'
data_file = 'data/day-01.txt'


def process(file):
    values = [int(x) for x in open(file).readlines()]
    part_1 = sum(b > a for a, b in [*zip(values, values[1:])])
    three = [*zip(values, values[1:], values[2:])]
    part_2 = sum(sum(b) > sum(a) for a,b in [*zip(three, three[1:])])

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 7
assert p2t == 5


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
