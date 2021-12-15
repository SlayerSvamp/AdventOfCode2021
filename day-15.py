test_file = 'data/test/day-15.txt'
data_file = 'data/day-15.txt'


def adjacent(available, x, y):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        pos = (x+dx, y+dy)
        if pos in available:
            yield pos


def lowest_risk(lines, size):
    height = len(lines)
    width = len(lines[0])
    risks = {
        (x+width*xz, y+height*yz): ((int(cell) + xz + yz - 1) % 9) + 1
        for yz in range(size)
        for xz in range(size)
        for y, line in enumerate(lines)
        for x, cell in enumerate(line)
    }
    keys = set(risks)
    end = (width*size-1, height*size-1)
    visiting = {0: {(0, 0)}}
    visited = {(0, 0)}
    while visiting:
        risk = min(visiting)
        for pos in visiting.pop(risk):
            for adj in set(adjacent(keys, *pos)):
                new_risk = risk + risks[adj]
                if adj == end:
                    return new_risk
                if adj not in visited:
                    visited.add(adj)
                    visiting.setdefault(new_risk, set()).add(adj)


def process(file):
    lines = open(file).read().splitlines()

    part_1 = lowest_risk(lines, 1)
    part_2 = lowest_risk(lines, 5)

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 40, p1t
assert p2t == 315, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
