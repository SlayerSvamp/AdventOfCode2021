import sys

day, *args = sys.argv[1:]

assert day.isnumeric(), 'first parameter must be numerical value for day in december'
name = f'day-{day:0>2}'
py_file = open(f'{name}.py', 'a+')

data = '--nodata' not in args
parse = '--parse' in args
spaces = 4
indent = spaces * ' '

if data:
    test_file = f'data/test/{name}.txt'
    data_file = f'data/{name}.txt'
    open(test_file, 'a+')
    open(data_file, 'a+')
    py_file.writelines(map(lambda x: x+'\n', [
        f"test_file = '{test_file}'",
        f"data_file = '{data_file}'",
        '',
        *([
            '',
            'def parse(line):',
            f'{indent}return int(line)',
            '',
        ] if parse else []),
        '',
        f'def process(file):',
        *([
            f'{indent}lines = [*map(parse, open(file).read().splitlines())]',
        ] if parse else [
            f'{indent}lines = open(file).read().splitlines()',
        ]),
        '',
        f'{indent}part_1 = 0',
        f'{indent}part_2 = 0',
        '',
        f'{indent}return [part_1, part_2]',
        '',
        '',
        'p1t, p2t = process(test_file)',
        'assert p1t == 0, p1t',
        'assert p2t == 0, p2t',
        '',
        '',
        'p1, p2 = process(data_file)',
        '',
        "print('Part 1:', p1)",
        "print('Part 2:', p2)",
    ]))
