from time import perf_counter
test_file = 'data/test/day-23.txt'
data_file = 'data/day-23.txt'

room_x = (2, 4, 6, 8)
home_x = dict(zip('ABCD', room_x))
outside = set(zip(room_x, (0, 0, 0, 0)))
costs = dict(zip('ABCD', (1, 10, 100, 1000)))


def timer(overwrite=False):
    def wrapper(f):
        def inner(*args, **kwargs):
            print_args = [*map(str, args)]
            print_args += [f'{key}={value}' for key, value in kwargs.items()]
            signature = f'{f.__name__}({", ".join(print_args)})'
            print(f'{signature} running...')
            start = perf_counter()
            res = f(*args, **kwargs)
            end = perf_counter()
            if overwrite:
                print(end='\33[1A\r')
            print(f'{signature} took {end-start:.2f} seconds')
            return res
        return inner
    return wrapper


def adjacent(current, x, y):
    seen = set()
    pod = current[x, y]
    home = home_x[pod]

    def inner(_x, _y):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_pos = _x+dx, _y+dy
            nx, ny = new_pos
            if new_pos in seen:
                continue
            if new_pos in current and current[new_pos] == '.':
                seen.add(new_pos)
                yield from inner(*new_pos)
                if new_pos in outside or bool(y) == bool(ny) or (ny and nx != home):
                    continue
                if ny and any(pd != pod and py > ny and nx == px for (px, py), pd in current.items()):
                    continue

                yield new_pos

    yield from inner(x, y)


@timer()
def process(file):
    raw = open(file).read()

    @timer(True)
    def run_part(part):
        lines = raw.splitlines()
        if part == 2:
            lines.insert(3, '  #D#C#B#A#')
            lines.insert(4, '  #D#B#A#C#')
        coords = {
            (x-1, y-1): cell
            for y, line in enumerate(lines)
            for x, cell in enumerate(line)
            if cell in 'ABCD.'
        }
        all_home = tuple(sorted(
            ((x, y), c)
            for x, y in coords
            if not y or x in room_x
            for c in '.ABCD'
            if (not y and c == '.') or (y and x == home_x.get(c))
        ))
        stack = [(0, coords)]
        seen = {}
        while stack:
            spent, step = stack.pop()
            for pos in step:
                pod = step[pos]
                x, y = pos
                if pod != '.':
                    if x == home_x[pod] and y:
                        by = y+1
                        while (x, by) in step:
                            if step[x, by] != pod:
                                break
                            by += 1
                        else:
                            continue

                    for nx, ny in adjacent(step, *pos):
                        cost = spent + (abs(x-nx) + abs(y-ny))*costs[pod]
                        next_step = dict(step)
                        next_step[nx, ny] = pod
                        next_step[x, y] = '.'
                        state = tuple(sorted(next_step.items()))
                        if state in seen and seen[state] <= cost:
                            continue
                        seen[state] = cost
                        stack.append((cost, next_step))
        return seen[all_home]

    part_1 = run_part(1)
    part_2 = run_part(2)

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 12521, p1t
assert p2t == 44169, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
