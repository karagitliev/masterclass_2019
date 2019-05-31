import os
from random_test_generator import create_new_test
import db_handler as db

os.system('clear')


print('ONE DOES NOT SIMPLY SOLVE THE TASK\n\n')


def main_menu():
    db.update_db()

    print('Please choose an option\n-----------------------\n')
    print('1 - Run one or multiple tests')
    print('2 - Run one or more tests manually')
    print('3 - Generate new random test')
    print('4 - Run ALL tests')
    print('\n5 - Quit\n')

    usr_choice = input('Enter number: ')

    if usr_choice == '1':
        print('\nAvailable tests in database\n---------------------------')
        all_tests = db.read_db('show_all')
        print(*all_tests, sep=' ')

        print('\nType the name or names(separated by whitespace) of the tests:\n')
        usr_choice = input()

    elif usr_choice == '2':
        pass
    elif usr_choice == '3':
        print(f'\n{create_new_test()}\n')
        # usr_choice = input('Would you like to run it? Y/n\n')
        # if usr_choice.upper() == 'Y':
        #    pass
    elif usr_choice == '4':
        pass
    elif usr_choice == '5':
        exit()


main_menu()
