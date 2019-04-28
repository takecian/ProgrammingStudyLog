# https://atcoder.jp/contests/abc125/tasks/abc125_c

import itertools
from collections import Counter
from collections import defaultdict
import bisect

memo = {}


def gcd(a, b):
    if a in memo:
        if b in memo[a]:
            return memo[a][b]
    ans = gcd_core(a, b)
    if a in memo:
        memo[a][b] = ans
    else:
        memo[a] = {}
        memo[a][b] = ans
    return ans


def gcd_core(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    answers = []
    # half
    m = N // 2
    ans1 = 0
    for i in range(m):
        ans1 = gcd(A[i], ans1)

    ans2 = 0
    for i in range(m, N):
        ans2 = gcd(A[i], ans2)

    for i in range(m, N):
        ans = ans1
        for j in range(m, N):
            if i == j:
                continue
            ans = gcd(A[j], ans)
        answers.append(ans)

    for i in range(m):
        ans = ans2
        for j in range(m):
            if i == j:
                continue
            ans = gcd(A[j], ans)
        answers.append(ans)

    print(max(answers))


if __name__ == '__main__':
    main()
