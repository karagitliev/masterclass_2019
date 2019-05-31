import random
import db_handler as db


def rand_color():
    colors = {
        1: 'R',
        2: 'G',
        3: 'B',
    }

    return colors[random.randint(1, 3)]


# FIXME add spaces between the colors
def create_new_test():
    rows = random.randint(5, 50)
    cols = random.randint(5, 50)

    matrix = ''
    for row in range(0, rows):
        m_str = ''
        for col in range(0, cols):
            m_str += ' '.join(rand_color())

        matrix += m_str + '\n'

    return db.create_file(matrix, rows, cols)
