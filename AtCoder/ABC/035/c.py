# https://atcoder.jp/contests/abc035/tasks/abc035_c

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n, q = map(int, input().split())
    proc = []
    for _ in range(q):
        l, r = map(int, input().split())
        proc.append((l - 1, r - 1))

    proc.sort(key=lambda x: (x[0], x[1]))
    ans = [0] * (n + 1)
    for l, r in proc:
        ans[l] += 1
        ans[r + 1] -= 1

    for i in range(n - 1):
        ans[i + 1] += ans[i]
    # print(ans)

    for i in range(n):
        ans[i] = 1 if ans[i] % 2 == 1 else 0

    print(''.join(map(str, ans[:-1])))


if __name__ == '__main__':
    main()
