# https://atcoder.jp/contests/abc047/tasks/arc063_a
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    s = input()
    if len(s) == 0 or s.count('W') == 0 or s.count('B') == 0:
        print(0)
        return

    pre = s[0]

    ans = 0
    for i in range(1, len(s)):
        if pre != s[i]:
            ans += 1
        pre = s[i]
    print(ans)


if __name__ == '__main__':
    main()
