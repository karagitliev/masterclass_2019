STEPS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def sequence_path(grid, x, y, m, n, key):  # dfs
    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != key:
        return 0
    count = 1
    grid[x][y] = 0
    for i, j in STEPS:
        count += sequence_path(grid, x + i, y + j, m, n, key)
    return count


def longest_sequence(grid, key):
    result = 0
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == key:
                result = max(result, sequence_path(grid, i, j, m, n, key))

    return result


# FIXME add multiple tests input and outp
# FIXME if two tests are initialised, outp returns sum ot them
def parse_file(data, type=None):
    grid = []
    uniq = {}

    data.pop(0)
    for i in range(len(data)):
        t_name = i
        f = open(data[i])

        dimension = f.readline().split(' ')
        n = int(dimension[0])
        m = int(dimension[1])

        for i in range(n):
            line = f.readline().replace('\n', '')
            ltrs = line.split()

            # convert ltrs to nums
            nums = []
            for ltr in ltrs:
                nums.append(ord(ltr))
                uniq[ltr] = 0  # get unique values here
            grid.append(nums)

        f.close()

        longest = []
        if len(uniq) == 1:  # if matrix contains only 1 symbol
            print(n * m)
        else:
            for key in uniq:
                longest.append(longest_sequence(grid, ord(key)))

        if longest:
            if type == 'menu':
                print(f'\n{data[t_name]}\nLongest adjacent sequence: {max(longest)}\n')
            else:
                print(max(longest))
