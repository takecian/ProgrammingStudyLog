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

    ming = 0

    cand = []

    for i in range(N):
        temp = gcd(A[i], ming)
        # print(temp)
        if temp != ming:
            cand.append(i)
        ming = temp

    # print(index)

    answers = []
    for c in cand:
        ans1 = 0
        for i in range(N):
            if i != c:
                ans1 = gcd(A[i], ans1)
        answers.append(ans1)

    print(max(answers))


if __name__ == '__main__':
    main()
