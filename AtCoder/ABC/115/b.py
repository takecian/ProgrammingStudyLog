# https://atcoder.jp/contests/abc115/tasks/abc115_b

N = int(input())

p = [int(input()) for _ in range(N)]

p.sort()

p[-1] = int(p[-1]/2)

print(sum(p))
