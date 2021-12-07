from functools import cache


test_file = 'data/test/day-07.txt'
data_file = 'data/day-07.txt'


def process(file):
    crabs = [*map(int, open(file).read().split(','))]
    viable = range(min(crabs), max(crabs))

    cache = {}

    def costs(cost):
        return [sum(cost(abs(crab-pos)) for crab in crabs) for pos in viable]
        
    def cumulative(n):
        if n not in cache:
            cache[n] = sum(range(n+1))
        return cache[n]


    part_1 = min(costs(int))
    part_2 = min(costs(cumulative))

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 37, p1t
assert p2t == 168, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
