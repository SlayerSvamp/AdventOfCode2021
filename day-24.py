data_file = 'data/day-24.txt'


def process(file):
    lines = open(file).read().splitlines()

    stack = []
    ranges = []
    for i, line in enumerate(lines):
        args = line.split(' ')
        step = i % 18
        segment = i // 18

        # set if push or pop
        if step == 4:
            div = args[-1]

        # push to stack
        if step == 15 and div == '1':
            stack.append((segment - len(stack), int(args[-1])))

        # pop from stack and calculate ranges
        if step == 5 and div == '26':
            target, value = stack.pop()
            value += int(args[-1])
            val = abs(value) + 1
            sign = -1 if value < 0 else 1
            base, relative = [(1, 10-val), (val, 9)][::sign]

            ranges.insert(target, base)
            ranges.append(relative)

    part_1 = ''.join(str(high) for _, high in ranges)
    part_2 = ''.join(str(low) for low, _ in ranges)

    return [part_1, part_2]


p1, p2 = process(data_file)
# Assert values taken from result in markdown.
# I completed the markdown solution before attempting this one.
assert p1 == '12934998949199', p1
assert p2 == '11711691612189', p2

print('Part 1:', p1)
print('Part 2:', p2)
