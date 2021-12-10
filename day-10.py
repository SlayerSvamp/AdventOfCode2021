test_file = 'data/test/day-10.txt'
data_file = 'data/day-10.txt'


def evaluate(line):
    opening = '([{<'
    closing = ')]}>'
    opened = []
    errors = []
    for x in line:
        if x in opening:
            opened.append(opening.index(x))
        else:
            if opened:
                if opened[-1] == closing.index(x):
                    opened.pop()
                else:
                    errors.append(closing.index(x))
    return [errors, opened]


def process(file):
    chunks = open(file).read().splitlines()
    points = [3, 57, 1197, 25137]
    error_score = 0
    incomplete = []

    for line in chunks:
        errors, left = evaluate(line)
        if errors:
            error_score += points[errors[0]]
        else:
            score = 0
            while left:
                score *= 5
                score += left.pop() + 1
            incomplete.append(score)

    part_1 = error_score
    part_2 = sorted(incomplete)[len(incomplete) // 2]

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 26397, p1t
assert p2t == 288957, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
