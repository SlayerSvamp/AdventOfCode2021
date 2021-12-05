test_file = 'data/test/day-05.txt'
data_file = 'data/day-05.txt'


def parse(line):
    return [*map(int, line.replace(' -> ', ',').split(','))]


def coords(start, stop):
    direction = 1
    if start > stop:
        direction = -1
        start, stop = stop, start
    values = [*range(start, stop + 1)][::direction]
    while True:
        yield from values


def count_overlaps(lines, diagonals):
    grid = {}
    for x1, y1, x2, y2 in lines:
        if diagonals or x1 == x2 or y1 == y2:
            length = max(abs(x1-x2), abs(y1-y2)) + 1
            x_coords = coords(x1, x2)
            y_coords = coords(y1, y2)
            for x, y, _ in zip(x_coords, y_coords, range(length)):
                grid[x, y] = grid.get((x, y), 0) + 1

    return sum(n > 1 for n in grid.values())


def process(file):
    lines = [*map(parse, open(file).read().splitlines())]
    part_1 = count_overlaps(lines, False)
    part_2 = count_overlaps(lines, True)

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 5, p1t
assert p2t == 12, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
