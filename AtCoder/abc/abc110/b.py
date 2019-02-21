# https://atcoder.jp/contests/abc110/tasks/abc110_b

N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x.sort()
y.sort()

if x[-1] < y[0]:
    for i in range(x[-1]+1, y[0]+1):
        if X < i <= Y:
            # print("X({}) < i({}) <= Y({})".format(X, i, Y))
            print("No War")
            exit()

print("War")
