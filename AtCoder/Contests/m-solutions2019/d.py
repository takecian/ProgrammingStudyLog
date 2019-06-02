#

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    N = int(input())
    d = [0] * N
    multi = [0] * N

    edges = defaultdict(list)
    edges_l = []
    for _ in range(N-1):
        a, b = map(int, input().split())
        d[a-1] += 1
        d[b-1] += 1
        multi[a-1] += 1
        multi[b-1] += 1

        edges_l.append((a-1, b-1))
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)

    for i in range(len(d)):
        d[i] = (d[i], i)
    d.sort(key=lambda v: v[0], reverse=True)

    C = list(map(int, input().split()))
    C.sort(reverse=True)
    # print(d)
    # print(C)
    used = [False] * N
    ans = [0] * N
    count = 0
    que = []
    que.append(d[0][1])
    while que:
        index = que.pop()
        if not used[index]:
            # print('i = {}, Ci = {}'.format(i, C[i]))
            ans[index] = C[count]
            used[index] = True
            count += 1

        # print(edges[i])
        for nei in edges[index]:
            if not used[nei]:
                que.append(nei)

    val = 0
    for a, b in edges_l:
        node_val = min(ans[a], ans[b])
        val += node_val

    print(val)
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
