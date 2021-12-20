test_file = 'data/test/day-20.txt'
data_file = 'data/day-20.txt'


def adjacent(grid, x, y, infinite):
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            yield grid.get((x+dx, y+dy), infinite)


def process(file):
    lines = open(file).read().splitlines()
    lookup = lines.pop(0)
    lines.pop(0)

    image = {}
    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            image[x, y] = cell

    for y in range(-50, len(lines) + 51):
        for x in range(-50, len(lines[0]) + 51):
            image[x, y] = image.get((x, y), '.')

    for pairs in range(25):
        for infinite in (0, lookup[0]):
            new_image = {}
            for (x, y), v in image.items():
                index = 0
                for z in adjacent(image, x, y, infinite):
                    index += index + (z == '#')
                new_image[x, y] = lookup[index]
            image = new_image
        if not pairs:
            part_1 = list(image.values()).count('#')
    part_2 = list(image.values()).count('#')

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 35, p1t
assert p2t == 3351, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
