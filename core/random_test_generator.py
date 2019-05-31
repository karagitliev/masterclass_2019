import os
import re
import random


def create_file(test_data):
    test_dir = 'tests'
    files = os.listdir(test_dir)

    tests = []
    for file in files:
        test_num = re.sub('\D', '', file)
        tests.append(test_num)

    new_test = int(max(tests)) + 1
    f = open(f'{test_dir}/test_{new_test}', "w+")

    f.write(test_data)
    return f'test_{new_test} was created successfully'


def rand_color():
    colors = {
        1: 'R',
        2: 'G',
        3: 'B',
    }

    return colors[random.randint(1, 3)]


def create_new_test():
    rows = random.randint(3, 50)
    cols = random.randint(3, 50)

    matrix = ''
    for row in range(0, rows):
        m_str = ''
        for col in range(0, cols):
            m_str += ' '.join(rand_color())

        matrix += m_str + '\n'

    return create_file(matrix)
