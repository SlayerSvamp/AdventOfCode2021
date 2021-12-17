import re
from itertools import count

test_file = 'data/test/day-17.txt'
data_file = 'data/day-17.txt'


def process(file):
    data = open(file).read()
    xmin, xmax, ymax, ymin = map(int, re.findall(r'-?\d+', data))

    ys = []
    for start in range(ymax, (1 - ymax)*3):
        local_max = start
        ypos = 0
        for i in count():
            ypos += start - i
            local_max = max(local_max, ypos)
            if ypos >= ymax:
                if ypos <= ymin:
                    ys.append((start, i, local_max))
            else:
                break

    max_y = 0
    seen = set()
    for x in range(xmax + 1):
        for y, i, local_max in ys:
            xpos = sum(range(x+1)) - sum(range(x-i))
            if xpos >= xmin and xpos <= xmax:
                max_y = max(max_y, local_max)
                seen.add((x, y))

    part_1 = max_y
    part_2 = len(seen)

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 45, p1t
assert p2t == 112, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
