test = 'data/test/day-02.txt'
data = 'data/day-02.txt'


def process(file):
    aim, horizontal, depth = 0, 0, 0

    for line in open(file).readlines():
        direction, value = line.split(' ')
        value = int(value)

        if direction == 'up':
            aim -= value
            
        if direction == 'down':
            aim += value

        if direction == 'forward':
            horizontal += value
            depth += aim * value

    return [aim * horizontal, depth * horizontal]


p1t, p2t = process(test)

assert p1t == 150
assert p2t == 900

p1, p2 = process(data)

print('Part 1:', p1)
print('Part 2:', p2)
