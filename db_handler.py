import os
import json
import time

TESTS_INFO = 'database/tests_info.txt'
DB_DIR = 'database'
TESTS_DIR = 'tests'


def update_db():
    files = os.listdir(TESTS_DIR)

    with open(TESTS_INFO) as f:
        data = json.load(f)

    for file in files:
        if file not in data:
            test_info = {
                file: {
                    'update_time': time.time(),
                    'used': 'NO',
                    'matrix_params': '',
                }
            }
            data[file] = test_info

    with open(TESTS_INFO, 'w') as outfile:
        json.dump(data, outfile, indent=4)


def read_file():
    with open(TESTS_INFO) as f:
        data = json.load(f)

        print(data)


def write_file(test_data):
    files = os.listdir(TESTS_DIR)

    tests = []
    for file in files:
        (prefix, test_num) = file.split('_')
        tests.append(test_num)

    new_test = int(max(tests)) + 1
    test_name = 'test_' + str(new_test)
    f = open(f'{TESTS_DIR}/{test_name}', "w+")

    f.write(test_data)

    test_info = {
        test_name: {
            'create_time': time.time(),
            'used': 'NO',
            'matrix_params': f'{rows} rows by {cols} cols',
        }
    }
    update_db(test_info)

    return f'test_{new_test} was created successfully'
