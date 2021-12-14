test_file = 'data/test/day-14.txt'
data_file = 'data/day-14.txt'


# written to solve part 1
def transform(polymer, pairs, steps):
    for _ in range(steps):
        inserts = {}
        for i in range(len(polymer) - 1):
            p = polymer[i:i+2]
            if p in pairs:
                inserts[i+1] = pairs[p]
        for i in sorted(inserts)[::-1]:
            polymer = polymer[:i] + inserts[i] + polymer[i:]

    r = [polymer.count(c) for c in set(polymer)]
    return max(r) - min(r)


# new solution after polymer size grew out of proportion
def track_count(polymer, pairs, steps):
    pair_count = {p: polymer.count(p) for p in pairs}
    element_count = {e: polymer.count(e) for e in pairs.values()}
    splitting_pairs = {
        (a+b): (a+insert, insert+b)
        for (a, b), insert in pairs.items()
    }
    for _ in range(steps):
        new_pair_count = {p: 0 for p in pairs}
        for pair, count in pair_count.items():
            inserted = pairs[pair]
            element_count[inserted] += count
            for new_pair in splitting_pairs[pair]:
                new_pair_count[new_pair] += count
        pair_count = new_pair_count

    counts = element_count.values()
    return max(counts) - min(counts)


def process(file):
    lines = open(file).read().splitlines()
    polymer = lines[0]
    pairs = dict(line.split(' -> ') for line in lines[2:])

    part_1 = transform(polymer, pairs, 10)
    part_2 = track_count(polymer, pairs, 40)

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 1588, p1t
assert p2t == 2188189693529, p2t

p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
