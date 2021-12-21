test_file = 'data/test/day-21.txt'
data_file = 'data/day-21.txt'


def deterministic(players):
    players = [*players]
    score = [0, 0]
    i = 0
    die = 1
    while True:
        p = i % 2
        steps = 0
        for _ in range(3):
            steps += die
            die = (die % 100) + 1
        players[p] = (players[p] + steps) % 10
        score[p] += players[p] or 10
        i += 3
        if score[p] >= 1000:
            return i * score[1-p]


def dirac(players):
    cache = {}

    def inner(players, score, p, rolls):
        players = [*players]
        score = [*score]
        if rolls == 3:
            score[p] += players[p] or 10
            if score[p] >= 21:
                return (1-p, p)
            rolls = 0
            p ^= 1

        total = [0, 0]
        for _ in range(3):
            players[p] = (players[p] + 1) % 10
            state = tuple(players), tuple(score), p, rolls + 1
            cache[state] = (wins := cache.get(state) or inner(*state))
            total = map(sum, zip(total, wins))

        return tuple(total)

    return max(inner(players, (0, 0), 0, 0))


def process(file):
    lines = open(file).read().splitlines()
    players = tuple(int(x[-1]) for x in lines)

    part_1 = deterministic(players)
    part_2 = dirac(players)

    return [part_1, part_2]


p1t, p2t = process(test_file)
assert p1t == 739785, p1t
assert p2t == 444356092776315, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
