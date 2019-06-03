import random
import db_handler as db


def rand_color():
    colors = {
        1: 'R',
        2: 'G',
        3: 'B',
    }

    return colors[random.randint(1, 3)]


def create_new_test():
    rows = random.randint(25, 25)
    cols = rows

    matrix = ''
    for row in range(0, rows):
        col_arr = []
        for col in range(0, cols):
            col_arr.append(rand_color())

        matrix += ' '.join(col_arr) + '\n'

    return db.create_file(matrix, rows, cols)
