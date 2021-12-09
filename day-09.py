from functools import reduce


test_file = 'data/test/day-09.txt'
data_file = 'data/day-09.txt'


def parse(line):
    return [*map(int, line)]


def adjacent(grid, x, y):
    for dx, dy in [(0, -1), (-1, 0), (0, +1), (+1, 0)]:
        if (p := (x+dx, y+dy)) in grid:
            yield p


def get_basin(grid, point, seen):
    seen.add(point)
    yield point
    for p in adjacent(grid, *point):
        if p not in seen:
            yield from get_basin(grid, p, seen)


def process(file):
    lines = [*map(parse, open(file).read().splitlines())]

    grid = {(x, y): value for y, row in enumerate(lines)
            for x, value in enumerate(row) if value < 9}
    low_points = {}
    for p in grid:
        if all(grid[a] >= grid[p] for a in adjacent(grid, *p)):
            low_points[p] = grid[p]

    sizes = []
    for x in low_points:
        sizes.append(len([*get_basin(grid, x, set())]))

    part_1 = sum(v+1 for v in low_points.values())
    part_2 = reduce(lambda a, b: a*b, sorted(sizes)[-3:])

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 15, p1t
assert p2t == 1134, p2t


p1, p2 = process(data_file)


print('Part 1:', p1)
print('Part 2:', p2)
