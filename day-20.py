test_file = 'data/test/day-20.txt'
data_file = 'data/day-20.txt'


def adjacent(grid, x, y, infinite):
    index = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            index += index + ('#' == grid.get((x+dx, y+dy), infinite))
    return index


def process(file):
    lines = open(file).read().splitlines()
    lookup = lines.pop(0)
    lines.pop(0)
    height = len(lines)
    width = len(lines[0])
    image = {}
    for y in range(-50, height + 51):
        for x in range(-50, width + 51):
            if height <= y or y < 0 or width <= x or x < 0:
                cell = '.'
            else:
                cell = lines[y][x]
            image[x+50, y+50] = cell

    inf_lookup = '.' + lookup[0]
    images = [image]
    for steps in range(50):
        infinite = inf_lookup[steps % 2]
        image = {}
        for x, y in images[-1]:
            index = adjacent(images[-1], x, y, infinite)
            image[x, y] = lookup[index]
        images.append(image)

    part_1 = list(images[2].values()).count('#')
    part_2 = list(images[-1].values()).count('#')

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 35, p1t
assert p2t == 3351, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
