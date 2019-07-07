# https://atcoder.jp/contests/abc133/tasks/abc133_e

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    mod = 10 ** 9 + 7
    n, k = map(int, input().split())

    edges = defaultdict(list)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)

    # print(edges)
    patterns = [-1] * n
    # dfs
    stack = deque()
    patterns[0] = k

    rest = k - 1
    for neighbor in edges[0]:
        patterns[neighbor] = max(0, rest)
        rest -= 1
        stack.append(neighbor)

    while len(stack) > 0:
        node = stack.pop()

        rest = k - 2
        for neighbor in edges[node]:
            if patterns[neighbor] == -1:
                patterns[neighbor] = max(0, rest)
                rest -= 1
                stack.append(neighbor)

    ans = 1
    for p in patterns:
        ans = ans * p % mod

    print(ans)


if __name__ == '__main__':
    main()
