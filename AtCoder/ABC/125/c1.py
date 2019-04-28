# https://atcoder.jp/contests/abc125/tasks/abc125_c

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

def main():
    N = int(input())
    A = list(map(int, input().split()))

    answers = []
    for i in range(N):
        ans = 0
        for j in range(len(A)):
            if i == j:
                continue
            ans = gcd(A[j], ans)
        answers.append(ans)

    print(max(answers))


if __name__ == '__main__':
    main()
