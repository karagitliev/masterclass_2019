import os
import json
import time

TESTS_INFO = 'database/tests_info.txt'
DB_DIR = 'database'
TESTS_DIR = 'tests'


def update_db(rows=None, cols=None):
    files = os.listdir(TESTS_DIR)

    with open(TESTS_INFO) as f:
        data = json.load(f)

    # FIXME update DB FILE if a test file is removed
    for file in files:
        if 'test_' not in file:
            continue

        (prefix, num) = file.split('_')
        if num not in data:
            test_info = {
                'file_name': file,
                'create_time': time.time(),
                'used': 'NO',
                'matrix_params': f'{rows} rows by {cols} cols',
            }
            data[num] = test_info

    with open(TESTS_INFO, 'w+') as outfile:
        json.dump(data, outfile, indent=4)


def read_db():
    with open(TESTS_INFO) as f:
        data = json.load(f)

    last_test = max(data.keys())

    return int(last_test) + 1


def create_file(matrix, rows, cols):
    prefix = 'test_'
    new_test_num = str(read_db())
    new_test = prefix + new_test_num

    f = open(f'{TESTS_DIR}/{new_test}', "w+")

    test_data = f'{rows} {cols}\n'
    test_data += matrix
    f.write(test_data)

    update_db(rows, cols)

    return f'{new_test} was created successfully'
