test_file = 'data/test/day-11.txt'
data_file = 'data/day-11.txt'


def adjacent(octopuses, x, y):
    delta = (-1, 0, 1)
    for dy in delta:
        for dx in delta:
            adj = (x+dx, y+dy)
            if (dx or dy) and adj in octopuses:
                yield adj


def process(file):
    lines = open(file).read().splitlines()
    octopuses = {
        (x, y): int(energy)
        for (y, line) in enumerate(lines)
        for (x, energy) in enumerate(line)
    }
    waves = []
    while sum(octopuses.values()):
        flashing = set()
        observed = list(octopuses)
        while observed:
            octo_pos = observed.pop()
            octopuses[octo_pos] += 1
            if octopuses[octo_pos] == 10:
                flashing.add(octo_pos)
                observed += adjacent(octopuses, *octo_pos)

        for octo_pos in flashing:
            octopuses[octo_pos] = 0

        waves.append(len(flashing))

    part_1 = sum(waves[:100])
    part_2 = len(waves)

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 1656, p1t
assert p2t == 195, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
