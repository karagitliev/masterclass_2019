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


def parse_file(f_name, type=None):
    grid = []
    uniq = {}

    with open(f_name) as f:
        n, m = f.readline().split(' ')
        n, m = int(n), int(m)

        for i in range(n):
            line = f.readline().replace('\n', '')
            ltrs = line.split()

            # convert ltrs to nums
            nums = []
            for ltr in ltrs:
                nums.append(ord(ltr))
                uniq[ltr] = 0  # get unique values here
            grid.append(nums)

    if len(uniq) == 1:  # if matrix contains only 1 symbol
        if type == 'menu':
            print(f'\n{f_name}\nLongest adjacent sequence: {n * m}\n')
        else:
            print(n * m)
    else:
        longest = []

        for key in uniq:
            longest.append(longest_sequence(grid, ord(key)))

        if longest:
            if type == 'menu':
                print(f'\n{f_name}\nLongest adjacent sequence: {max(longest)}\n')
            else:
                print(max(longest))
