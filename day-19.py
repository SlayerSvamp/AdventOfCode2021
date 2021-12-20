test_file = 'data/test/day-19.txt'
data_file = 'data/day-19.txt'


def direct(coordinates):
    for directions in [(1, 1, 1), (-1, -1, 1), (-1, 1, -1), (1, -1, -1)]:
        for order in [-1, 1]:
            for rotation in range(3):
                result = []
                for coord in coordinates:
                    coord = [c*d for c, d in zip(coord, directions)]
                    coord = coord[rotation:] + coord[:rotation]
                    coord = coord[::order]
                    coord[0] = coord[0] * order
                    result.append(tuple(coord))
                yield result


def check_for_overlap(found, relative, limit):
    deltas = {}
    for A in found:
        for R in relative:
            delta = tuple(r-a for a, r in zip(A, R))
            deltas.setdefault(delta, 0)
            deltas[delta] += 1
            if deltas[delta] >= limit:
                dx, dy, dz = delta
                return delta, {(x-dx, y-dy, z-dz) for x, y, z in relative}


def next_overlap(scanners, found):
    for scanner, coordinates in scanners.items():
        for coords in direct(coordinates):
            if res := check_for_overlap(found, coords, 12):
                delta, new_found = res
                return scanner, new_found, delta


def process(file):
    groups = open(file).read().split('\n\n')
    scanners = {}
    for group in groups:
        lines = group.splitlines()
        name = int(lines.pop(0).split(' ')[2])
        scanners[name] = []
        for line in lines:
            coord = tuple(map(int, line.split(',')))
            scanners[name].append(coord)

    found = set(scanners[0])
    del scanners[0]
    deltas = [(0, 0, 0)]
    while scanners:
        overlap = next_overlap(scanners, found)
        scanner, new_found, delta = overlap
        deltas.append(delta)
        found |= new_found
        del scanners[scanner]

    maxhattan = 0
    for dx1, dy1, dz1 in deltas:
        for dx2, dy2, dz2 in deltas:
            diff = abs(dx1-dx2) + abs(dy1-dy2) + abs(dz1-dz2)
            maxhattan = max(maxhattan, diff)

    part_1 = len(found)
    part_2 = maxhattan

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 79, p1t
assert p2t == 3621, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
