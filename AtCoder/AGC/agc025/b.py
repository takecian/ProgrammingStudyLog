# note solved
#  https://agc025.contest.atcoder.jp/tasks/agc025_b
import math


p_cache = {}

def factorial(n):
    if n in p_cache:
        return p_cache[n]
    p_cache[n] = math.factorial(n)

    return p_cache[n]


c_cache = {}

def combinations_count(n, r):
    if r == 0:
        return 1
    if n in c_cache and r in c_cache[n]:
        return c_cache[n][r]
    else:
        if n not in c_cache:
            c_cache[n] = {}
        c_cache[n][r] = factorial(n) // (factorial(n - r) * factorial(r))
    return c_cache[n][r]


N, A, B, K = map(int, input().split())

if K == 0:
    print(1)
    exit(0)

RED = A
GREEN = A + B
BLUE = B


candidates = []

a_count = 0
val = K
while val >= 0:
    if val % B == 0:
        b_count = val // B
        if a_count <= N and b_count <= N and a_count * RED + b_count * BLUE == K:
            candidates.append((a_count, b_count))

    val -= A
    a_count += 1


# print(candidates)


total = 0
for c in candidates:
    a_pattern = combinations_count(N, c[0])
    b_pattern = combinations_count(N, c[1])
    total += a_pattern * b_pattern

print(total % 998244353)
