# https://paiza.jp/challenges/14/show

board = [[' ' for i in range(8)] for j in range(8)]

board[3][3] = 'W'
board[3][4] = 'B'
board[4][3] = 'B'
board[4][4] = 'W'

steps = []


def calc(board, c, x, y):
    # check 8 directions
    target = 'W' if c == 'B' else 'B'
    candidates = []

    # minus x
    minus_x = x - 1
    l_candidates = []
    while minus_x >= 0 and board[minus_x][y] == target:
        l_candidates.append({'x': minus_x, 'y': y})
        minus_x -= 1s
    if minus_x >= 0 and board[minus_x][y] == c:
        candidates.extend(l_candidates)

    # minus y
    minus_y = y - 1
    l_candidates = []
    while minus_y >= 0 and board[x][minus_y] == target:
        l_candidates.append({'x': x, 'y': minus_y})
        minus_y -= 1
    if minus_y >= 0 and board[x][minus_y] == c:
        candidates.extend(l_candidates)

    # plus x
    plus_x = x + 1
    l_candidates = []
    while plus_x < 8 and board[plus_x][y] == target:
        l_candidates.append({'x': plus_x, 'y': y})
        plus_x += 1
    if plus_x < 8 and board[plus_x][y] == c:
        candidates.extend(l_candidates)

    # plus y
    plus_y = y + 1
    l_candidates = []
    while plus_y < 8 and board[x][plus_y] == target:
        l_candidates.append({'x': x, 'y': plus_y})
        plus_y += 1
    if plus_y < 8 and board[x][plus_y] == c:
        candidates.extend(l_candidates)

    # minus x  minus y
    minus_y = y - 1
    minus_x = x - 1
    l_candidates = []
    while minus_x >= 0 and minus_y >= 0 and board[minus_x][minus_y] == target:
        l_candidates.append({'x': minus_x, 'y': minus_y})
        minus_x -= 1
        minus_y -= 1
    if minus_x >= 0 and minus_y >= 0 and board[minus_x][minus_y] == c:
        candidates.extend(l_candidates)

    # minus x  plus y
    plus_y = y + 1
    minus_x = x - 1
    l_candidates = []
    while minus_x >= 0 and plus_y < 8 and board[minus_x][plus_y] == target:
        l_candidates.append({'x': minus_x, 'y': plus_y})
        minus_x -= 1
        plus_y += 1
    if minus_x >= 0 and plus_y < 8 and board[minus_x][plus_y] == c:
        candidates.extend(l_candidates)

    # plus x  minus y
    minus_y = y - 1
    plus_x = x + 1
    l_candidates = []
    while plus_x < 8 and minus_y >= 0 and board[plus_x][minus_y] == target:
        l_candidates.append({'x': plus_x, 'y': minus_y})
        plus_x += 1
        minus_y -= 1
    if plus_x < 8 and minus_y >= 0 and board[plus_x][minus_y] == c:
        candidates.extend(l_candidates)

    # plus x  plus y
    plus_y = y + 1
    plus_x = x + 1
    l_candidates = []
    while plus_x < 8 and plus_y < 8 and board[plus_x][plus_y] == target:
        l_candidates.append({'x': plus_x, 'y': plus_y})
        plus_x += 1
        plus_y += 1
    if plus_x < 8 and plus_y < 8 and board[plus_x][plus_y] == c:
        candidates.extend(l_candidates)


    for can in candidates:
        board[can['x']][can['y']] = c

    return board, len(candidates)


# for b in board:
#     print(b)

count = int(input())


for i in range(count):
    c, x, y = input().split()
    steps.append({'c': c, 'x': int(x)-1, 'y': int(y)-1})

# print(steps)
# print(count)

pass_count = 0

for step in steps:
    board[step['x']][step['y']] = step['c']
    # for b in board:
    #     print(b)
    # print("----------------------------------")
    board, changes = calc(board, step['c'], step['x'], step['y'])
    # for b in board:
    #     print(b)
    # print("----------------------------------")

    if changes == 0:
        pass_count += 1
    else:
        pass_count = 0

    if pass_count > 1:
        break # game finish

white_count = 0
black_count = 0
for x_line in board:
    for y_line in x_line:
        if y_line == 'W':
            white_count += 1
        if y_line == 'B':
            black_count += 1


if white_count > black_count:
    print('{0:02d}'.format(black_count) + "-" + '{0:02d}'.format(white_count) + ' The white won!')
elif white_count < black_count:
    print('{0:02d}'.format(black_count) + "-" + '{0:02d}'.format(white_count) + ' The black won!')
else:
    print('{0:02d}'.format(black_count) + "-" + '{0:02d}'.format(white_count) + ' Draw!')



