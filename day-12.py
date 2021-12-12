import tracemalloc
test_file = 'data/test/day-12.txt'
data_file = 'data/day-12.txt'


def process(file):
    connections = {}
    for line in open(file).read().splitlines():
        a, b = line.split('-')
        connections.setdefault(a, set()).add(b)
        connections.setdefault(b, set()).add(a)

    exploring = [(['start'], True)]
    reached_end = []
    while exploring:
        path, extra = exploring.pop()
        for cave in connections[path[-1]] - {'start'}:
            if cave == 'end':
                reached_end.append(extra)
            elif cave.isupper() or cave not in path:
                exploring.append(([*path, cave], extra))
            elif extra:
                exploring.append(([*path, cave], False))

    part_1 = sum(reached_end)
    part_2 = len(reached_end)

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 226, p1t
assert p2t == 3509, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
