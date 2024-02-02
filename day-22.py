import time
import re
test_file_1 = 'data/test/day-22.1.txt'
test_file_2 = 'data/test/day-22.2.txt'
data_file = 'data/day-22.txt'


def progress(total, length=20, *, title='', sep=': '):
    if title:
        title += sep
    start = time.perf_counter()

    def inner(done):
        elapsed = time.perf_counter() - start
        left = "#" * round((length * done) / total)
        right = " " * (length - len(left))
        bar = f'[{left}{right}]'
        print(f'\33[1A\r{title}{bar} - {elapsed:.3f}s')

    print()
    inner(0)
    return inner


def overlaps(target):
    def inner(item):
        _target = [*target]
        product = 1
        while _target and product:
            t1, t2, *_target = _target
            i1, i2, *item = item
            product *= max(min(t2, i2) + 1 - max(t1, i1), 0)
        return product
    return inner


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
    if overlaps(target)(item):
        parts = []
        target, *parts[0:] = cut_off(target, item, x1, x2)
        target, *parts[2:] = cut_off(target, item, y1, y2)
        target, *parts[4:] = cut_off(target, item, z1, z2)
        return list(filter(lambda x: x, parts))

    return [target]


def process(file):
    with open(file) as f:
        lines = f.read().splitlines()

    seen = set()
    length = len(lines)
    bar = progress(length, title=file)

    while lines:
        line = lines.pop(0)
        action, line = line.split(' ')
        ranges = tuple(map(int, re.findall(r'-?\d+', line)))

        processing = {(action == 'on', ranges)}
        while processing:
            on, item = processing.pop()
            run_for = overlaps(item)
            for target in seen:
                if run_for(target):
                    seen.remove(target)
                    seen |= set(map(tuple, cut(target, item)))
                    processing.add((on, item))
                    break
            else:
                if on:
                    seen.add(item)
        bar(length - len(lines))

    init_proc_area = (-50, 50, -50, 50, -50, 50)
    part_1 = sum(map(overlaps(init_proc_area), seen))
    part_2 = sum(map(lambda x: overlaps(x)(x), seen))

    return [part_1, part_2]


p1t, p2t = process(test_file_1)
assert p1t == 590784, p1t
p1t, p2t = process(test_file_2)
assert p1t == 474140, p1t
assert p2t == 2758514936282235, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
