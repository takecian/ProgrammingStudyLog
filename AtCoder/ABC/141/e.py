#
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n = int(input())
    s = input()
    if len(set(s)) == n:
        print(0)
        return

    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                if i > 0 and j > 0:
                    length = dp[i-1][j-1]
                    if j - length > i:
                        dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 1

    ans = 0
    for d in dp:
        ans = max(ans, max(d))
    print(ans)


if __name__ == '__main__':
    main()
