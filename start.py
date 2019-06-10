import os
import sys
import algorithm
import db_handler as db
from random_test_generator import create_new_test


def main_menu():
    db.update_db()

    menu = '''Please choose an option
-----------------------
1 - Run one or multiple tests from /tests
2 - Run one or more tests manually
3 - Generate new random test
4 - Quit
'''

    print(menu)

    usr_choice = input('Enter a number: ')
    menu_items = {
        '1': run_test(),
        '2': add_to_database(),
        '3': create_test(),
        '4': exit(),
    }
    menu_items[usr_choice]


def add_to_database():
    print('\nType the absolute path/s of the file/s(separated by whitespace):\n')
    usr_input = input().split()

    data = []
    for item in usr_input:
        os.system(f'cp {item} {db.TESTS_DIR}')
        item = item.split('/')[-1]
        data.append(item)

    db.update_db()
    run_test(data)


def run_test(new_test=None):
    if not new_test:
        print('\nAvailable tests in database\n---------------------------')
        all_tests = db.read_db('show_all')
        print(*all_tests, sep=' ')

        print('\nType the name/s (separated by whitespace)\n')
        usr_input = input().split()
    else:
        usr_input = new_test

    for item in usr_input:
        item = db.TESTS_DIR + item
        algorithm.parse_file(item, 'menu')


def create_test():
    new_test = db.TESTS_DIR + create_new_test()
    usr_choice = input(f'\n{new_test} was created, would you like to run it? Y/n\n')
    if usr_choice.upper() == 'Y':
        algorithm.parse_file(new_test, 'menu')
    else:
        main_menu()


if __name__ == "__main__" and len(sys.argv) == 1:
    os.system('clear')
    print('ONE DOES NOT SIMPLY SOLVE THE TASK\n')

    main_menu()
else:
    sys.argv.pop(0)
    for item in sys.argv:
        algorithm.parse_file(item, 'sys')
