import sys


sys.argv.pop(0)
for arg in (sys.argv):
    with open(f'tests/{arg}') as f:
        data = f.read().replace(' ', '')

    result = parse_matrix(data)
    # FIXME add test name and result in dict and print on finish


def parse_matrix(data):
    rows = data[0]
