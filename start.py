import os
import sys
import algorithm
import db_handler as db
from random_test_generator import create_new_test


# FIXME menu needs major refactoring, move choices to functions
def main_menu():
    db.update_db()

    print('\nPlease choose an option\n-----------------------\n')
    print('1 - Run one or multiple tests from /tests')
    print('2 - Run one or more tests manually')
    print('3 - Generate new random test')
    print('\n4 - Quit\n')

    usr_choice = input('Enter a number: ')

    if usr_choice == '1':
        run_test()
    elif usr_choice == '2':
        add_to_database()
    elif usr_choice == '3':
        create_test()
    elif usr_choice == '4':
        exit()


def add_to_database():
    print('\nType the absolute path or paths(separated by whitespace) of the test:\n')
    usr_input = input().split()

    data = []
    for item in usr_input:
        os.system(f'cp {item} {db.TESTS_DIR}')
        item = item.split('/')[-1]
        data.append(item)

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

    data = ['0']
    for item in usr_input:
        item = db.TESTS_DIR + item
        data.append(item)
    algorithm.parse_file(data)


def create_test():
    data = ['0']
    new_test = db.TESTS_DIR + create_new_test()
    data.append(new_test)
    usr_choice = input(f'\n{new_test} was created, would you like to run it? Y/n\n')
    if usr_choice.upper() == 'Y':
        algorithm.parse_file(data)
    else:
        main_menu()


if __name__ == "__main__" and len(sys.argv) == 1:
    os.system('clear')
    print('ONE DOES NOT SIMPLY SOLVE THE TASK\n')

    main_menu()
else:
    algorithm.parse_file(sys.argv)
