test_file = 'data/test/day-13.txt'
data_file = 'data/day-13.txt'


def process(file):
    dots_raw, instructions = open(file).read().split('\n\n')
    dots = set()
    for line in dots_raw.splitlines():
        x, y = map(int, line.split(','))
        dots.add((x, y))

    for line in instructions.splitlines():
        axis, pos = line.split(' ').pop().split('=')
        pos = int(pos)
        folded = set()
        for x, y in dots:
            if axis == 'x' and x > pos:
                x = pos*2 - x
            elif axis == 'y' and y > pos:
                y = pos*2 - y
            folded.add((x, y))
        dots = folded
        yield len(dots)

    yield dots


p1t, *_, p2t = process(test_file)
assert p1t == 17, p1t


p1, *_, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:')
Y = {y for _, y in p2}
X = {x for x, _ in p2}
for y in range(min(Y), max(Y)+1):
    for x in range(min(X), max(X)+1):
        c = f' {"♥♦♣♠"[(x-y) % 4]}'[(x, y) in p2]
        print(f'{c} ', end='')
    print()
