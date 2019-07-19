
def closewise(grid):
    ''' 転値して反転すると時計回り
    :param grid:
    :return:
    '''
    return list(map(list, list(zip(*grid))[::-1]))


def counter_closewise(grid):
    ''' 反転して転値すると反時計回り
    :param grid:
    :return:
    '''
    return list(map(list, list(zip(*grid[::-1]))))


grid1 = [[1,2,3], [4,5,6], [7,8,9]]

print('org')
for g in grid1:
    print(g)

print('clockwise')

for g in closewise(grid1):
    print(g)


print('counter clockwise')
for g in counter_closewise(grid1):
    print(g)

print('')
for g in counter_closewise(counter_closewise(grid1)):
    print(g)
