test_file = 'data/test/day-03.txt'
data_file = 'data/day-03.txt'


def get_common(bits, indices=None):
    bits = [int(x) for x in bits]
    if indices:
        bits = [x for i, x in enumerate(bits) if i in indices]
    return 1 if sum(bits) >= (len(bits)/2) else 0


def process(file):
    lines = open(file).read().splitlines()
    gamma = 0
    epsilon = 0
    oxygen = [*range(len(lines))]
    scrubber = [*range(len(lines))]

    for bits in zip(*lines):
        common = get_common(bits)
        gamma += gamma + common
        epsilon += epsilon + 1 - common

        common_oxygen = get_common(bits, oxygen)
        if len(oxygen) > 1:
            oxygen = [x for x in oxygen if int(bits[x]) == common_oxygen]
        
        common_scrubber = get_common(bits, scrubber)
        if len(scrubber) > 1:
            scrubber = [x for x in scrubber if int(bits[x]) != common_scrubber]

    part_1 = gamma * epsilon
    part_2 = int(lines[oxygen[0]], 2) * int(lines[scrubber[0]], 2)

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 198, p1t
assert p2t == 230, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
