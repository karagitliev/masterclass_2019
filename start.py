import os
import sys
import algorithm
import db_handler as db
from random_test_generator import create_new_test

os.system('clear')


print('ONE DOES NOT SIMPLY SOLVE THE TASK\n')


def main_menu():
    db.update_db()

    print('\nPlease choose an option\n-----------------------\n')
    print('1 - Run one or multiple tests from /tests')
    print('2 - Run one or more tests manually')
    print('3 - Generate new random test')
    print('\n4 - Quit\n')

    usr_choice = input('Enter a number: ')

    if usr_choice == '1':
        print('\nAvailable tests in database\n---------------------------')
        all_tests = db.read_db('show_all')
        print(*all_tests, sep=' ')

        print('\nType the name/s (separated by whitespace)\n')
        usr_choice = input().split()
        data = [0]
        for item in usr_choice:
            item = 'tests/' + item
            data.append(item)
        algorithm.parse_file(data)

    elif usr_choice == '2':
        print('\nType the absolute path or paths(separated by whitespace) of the test:\n')
        usr_choice = input()
    elif usr_choice == '3':
        print(f'\n{create_new_test()}\n')
        usr_choice = input('Would you like to run it? Y/n\n')
        if usr_choice.upper() == 'Y':
            pass
        else:
            main_menu()
    elif usr_choice == '4':
        exit()


if __name__ == "__main__" and len(sys.argv) == 1:
    main_menu()
else:
    algorithm.parse_file(sys.argv)
