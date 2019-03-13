# https://atcoder.jp/contests/aising2019/tasks/aising2019_b

N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))

f = 0
s = 0
t = 0

for p in P:
    if p <= A:
        f += 1
    elif p <= B:
        s += 1
    else:
        t += 1

print(min(f,s,t))
