# https://tdpc.contest.atcoder.jp/tasks/tdpc_contest

N = int(input())
P = [int(i) for i in input().split()]
L = [set() for _ in range(N+1)]

L[0].add(0)
for i in range(1, N+1):
    for a in L[i-1]:
        L[i].add(a)
        L[i].add(a+P[i-1])

print(len(L[N]))
