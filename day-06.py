test_file = 'data/test/day-06.txt'
data_file = 'data/day-06.txt'


def parse(value):
    return int(value)


def process(file):
    values = [*map(parse, open(file).read().split(','))]
    fish = {x: values.count(x) for x in range(9)}
    for i in range(256):
        cycled = fish[0]
        fish = {x-1: n for x, n in fish.items() if x}
        fish[6] += cycled
        fish[8] = cycled
        
        if i == 79:
            part_1 = sum(fish.values())
    part_2 = sum(fish.values())

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 5934, p1t
assert p2t == 26984457539, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
