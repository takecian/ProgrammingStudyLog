# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_d
import math

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

fixed = []

for i in range(len(A)):
    if A[i] in B:
        j = B.index(A[i])
        fixed.append((i, j))
    else:


# print(fixed)
free_position = N * M - len(fixed)
print(math.factorial(free_position))
