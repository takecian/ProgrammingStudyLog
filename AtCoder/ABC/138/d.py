#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n, q = map(int, input().split())
    edge = defaultdict(list)
    counter = [0] * n

    for _ in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append(b)

    for _ in range(q):
        p, x = map(int, input().split())
        p -= 1
        counter[p] += x

    que = deque()
    que.append(0)

    while len(que) > 0:
        node = que.popleft()
        for next in edge[node]:
            counter[next] += counter[node]
            que.append(next)

    print(' '.join(map(str, counter)))

if __name__ == '__main__':
    main()
