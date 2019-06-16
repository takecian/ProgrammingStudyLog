#

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    N = int(input())
    xy = []
    for _ in range(N):
        x, y = map(int, input().split())
        xy.append((x, y))

    if N == 1:
        print(1)
        exit()

    xy.sort(key=lambda p: (p[0], p[1]))
    # print(xy)

    cand = defaultdict(lambda:0)

    for i in range(N-1):
        for j in range(i+1, N):
            p = xy[j][0] - xy[i][0]
            q = xy[j][1] - xy[i][1]
            key = '{},{}'.format(p, q)
            cand[key] += 1
    counter = Counter(cand)
    pq_count = counter.most_common()[0][1]
    # print(counter.most_common()[0])
    print(N - pq_count)


if __name__ == '__main__':
    main()
