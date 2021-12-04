import re

test_file = 'data/test/day-04.txt'
data_file = 'data/day-04.txt'


def parse(lines):
    boards = []
    numbers, *lines = lines

    for line in lines:
        if not line:
            boards += [{}]
            row = 0
        else:
            nums = re.split(r'\s+', line.strip())
            for col, num in enumerate(nums):
                boards[-1][row, col] = num
            row += 1

    return numbers, boards


def process(file):
    lines = open(file).read().splitlines()
    numbers, boards = parse(lines)
    first = 0

    for current in numbers.split(','):
        for board in [*boards]:
            rows = {row for row, _ in board}
            cols = {col for _, col in board}

            for row, col in board:
                if board[row, col] == current:
                    board[row, col] = 0

                elif board[row, col]:
                    rows.discard(row)
                    cols.discard(col)

            if rows or cols:
                score = sum(map(int, board.values())) * int(current)
                boards.remove(board)
                if not first:
                    first = score

        if not boards:
            return [first, score]


p1t, p2t = process(test_file)
assert p1t == 4512, p1t
assert p2t == 1924, p2t


p1, p2 = process(data_file)

print('Part 1:', p1)
print('Part 2:', p2)
