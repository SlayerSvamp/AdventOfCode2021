test_file = 'data/test/day-16.txt'
data_file = 'data/day-16.txt'


def take_num(items, x):
    n, items = items[:x], items[x:]
    return int(n, 2), items


def unpack(bits):
    version_total, bits = take_num(bits, 3)
    type_id, bits = take_num(bits, 3)
    if type_id == 4:
        value = 0
        check = 0b10000
        mask = 0b01111
        while check:
            n, bits = take_num(bits, 5)
            value <<= 4
            value += n & mask
            check &= n
    else:
        packets = []
        len_id, bits = take_num(bits, 1)
        length, bits = take_num(bits, 11 if len_id else 15)
        if len_id:
            for _ in range(length):
                v, bits, value = unpack(bits)
                packets.append(value)
                version_total += v
        else:
            while length:
                length -= len(bits)
                v, bits, value = unpack(bits)
                packets.append(value)
                length += len(bits)
                version_total += v

        def mul(values):
            value = 1
            for v in values:
                value *= v
            return value

        def gt(ps): return ps[0] > ps[1]
        def lt(ps): return ps[0] < ps[1]
        def eq(ps): return ps[0] == ps[1]
        operations = [sum, mul, min, max, None, gt, lt, eq]
        value = operations[type_id](packets)

    return version_total, bits, value


def process(file):
    data_hex = open(file).read()
    binary = ''.join(format(int(x, 16), '04b') for x in data_hex)

    version_sum, _, value = unpack(binary)

    part_1 = version_sum
    part_2 = value

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 31, p1t
assert p2t == 54, p2t


p1, p2 = process(data_file)
assert p2 > 790474483631, p2
print('Part 1:', p1)
print('Part 2:', p2)
