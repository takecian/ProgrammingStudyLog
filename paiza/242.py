# https://paiza.jp/challenges/242/show

H, W = map(int, input().split())
a_11, a_12 = map(int, input().split())
a_21, a_22 = map(int, input().split())

# print(H)
# print(W)

dim = [[0 for x in range(W)] for y in range(H)]
dim[0][0] = a_11
dim[0][1] = a_12
dim[1][0] = a_21
dim[1][1] = a_22

# for d in dim:
#     print(d)

for y in range(2, H):
    for x in range(0, 2):
        dif = dim[y-1][x] - dim[y-2][x]
        dim[y][x] = dim[y-1][x] + dif

for y in range(0, H):
    for x in range(2, W):
        dif = dim[y][x-1] - dim[y][x-2]
        dim[y][x] = dim[y][x-1] + dif

for d in dim:
    l = list(map(str, d))
    print(' '.join(l))


