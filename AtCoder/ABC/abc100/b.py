# https://abc100.contest.atcoder.jp/tasks/abc100_b

D, N = map(int, input().split())

if N != 100:
    print(100 ** D * N)
else:
    print(100 ** D * (N + 1))

