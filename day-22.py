import re
test_file_1 = 'data/test/day-22.1.txt'
test_file_2 = 'data/test/day-22.2.txt'
data_file = 'data/day-22.txt'



def size(item):
    x1, x2, y1, y2, z1, z2 = item
    return (x2-x1+1) * (y2-y1+1) * (z2-z1+1)


def overlaps(target, item):
    def overlap(a1, a2, b1, b2):
        return max(min(a2, b2) + 1 - max(a1, b1), 0)

    tx1, tx2, ty1, ty2, tz1, tz2 = target
    ix1, ix2, iy1, iy2, iz1, iz2 = item

    if x := overlap(tx1, tx2, ix1, ix2):
        if y := overlap(ty1, ty2, iy1, iy2):
            z = overlap(tz1, tz2, iz1, iz2)
            return x * y * z
    return 0


def cut_off(target, item, start, end):
    before = None
    after = None
    if target[start] < item[start]:
        before = [*target]
        before[end] = item[start]-1
        target[start] = item[start]

    if target[end] > item[end]:
        after = [*target]
        after[start] = item[end]+1
        target[end] = item[end]

    return target, before, after


def cut(target, item):
    target = list(target)

    x1, x2, y1, y2, z1, z2 = [0, 1, 2, 3, 4, 5]
    if overlaps(target, item):
        parts = []
        target, *parts[0:] = cut_off(target, item, x1, x2)
        target, *parts[2:] = cut_off(target, item, y1, y2)
        target, *parts[4:] = cut_off(target, item, z1, z2)

        return list(filter(lambda x: x, parts))
    return [target]


def process(file):
    with open(file) as f:
        lines = f.read().splitlines()

    seen = []
    for line in lines:
        action, line = line.split(' ')
        ranges = tuple(map(int, re.findall(r'-?\d+', line)))

        processing = [(action == 'on', ranges)]
        while processing:
            on, item = processing.pop()
            
            for target in seen:
                if overlaps(target, item):
                    seen.remove(target)
                    for x in cut(target, item):
                        processing.append((True, x))
                    processing.append((on, item))
                    break
            else:
                if on:
                    seen.append(item)

    init_proc_area = (-50, 50, -50, 50, -50, 50)
    part_1 = sum(map(lambda x: overlaps(init_proc_area, x), seen))
    part_2 = sum(map(size, seen))

    return [part_1, part_2]


p1t, p2t = process(test_file_1)
assert p1t == 590784, p1t
p1t, p2t = process(test_file_2)
assert p1t == 474140, p1t
assert p2t == 2758514936282235, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
