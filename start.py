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
    print('1 - Run one or multiple tests')
    print('2 - Run one or more tests manually')
    print('3 - Generate new random test')
    print('4 - Run ALL tests')
    print('\n5 - Quit\n')

    usr_choice = input('Enter a number: ')

    if usr_choice == '1':
        print('\nAvailable tests in database\n---------------------------')
        all_tests = db.read_db('show_all')
        print(*all_tests, sep=' ')

        print('\nType the name or names(separated by whitespace) of the tests:\n')
        usr_choice = input()

    elif usr_choice == '2':
        print('\nType the absolute path or paths(separated by whitespace) of the tests:\n')
        usr_choice = input()
    elif usr_choice == '3':
        print(f'\n{create_new_test()}\n')
        usr_choice = input('Would you like to run it? Y/n\n')
        if usr_choice.upper() == 'Y':
            pass
        else:
            main_menu()
    elif usr_choice == '4':
        print('\nAvailable tests in database\n---------------------------')
        all_tests = db.read_db('show_all')
        print(*all_tests, sep=' ')

        usr_choice = input('\nType Y/n to continue\n')
        if usr_choice.upper() == 'Y':
            pass
        else:
            main_menu()
    elif usr_choice == '5':
        exit()


if __name__ == "__main__" and len(sys.argv) == 1:
    main_menu()
else:
    algorithm()
