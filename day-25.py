test_file = 'data/test/day-25.txt'
data_file = 'data/day-25.txt'


def process(file):
    lines = open(file).read().splitlines()
    cucumbers = {
        (y, x): cell
        for y, line in enumerate(lines)
        for x, cell in enumerate(line)
    }
    height = len(lines)
    width = len(lines[0])
    steps = 0
    moved = True
    while moved:
        moved = False
        eastcumbers = dict(cucumbers)
        for pos, state in cucumbers.items():
            if state == '>':
                y, x = pos
                forward = y, (x+1) % width
                if cucumbers[forward] == '.':
                    eastcumbers[forward] = '>'
                    eastcumbers[pos] = '.'
                    moved = True

        newcumbers = dict(eastcumbers)
        for pos, state in (eastcumbers.items()):
            if state == 'v':
                y, x = pos
                downward = (y + 1) % height, x
                if eastcumbers[downward] == '.':
                    newcumbers[downward] = 'v'
                    newcumbers[pos] = '.'
                    moved = True
        steps += 1
        cucumbers = newcumbers

    return steps


p1t = process(test_file)
assert p1t == 58, p1t


p1 = process(data_file)

print('Part 1:', p1)
print('Part 2: All done!')
