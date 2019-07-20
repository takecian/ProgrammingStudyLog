#

#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop
import math

def main():
    n = int(input())
    al = list(map(int, input().split()))

    ans = [0] * n

    half = math.ceil(n/2)
    for i in range(half, n):
        ans[i] = al[i]

    for i in range(half-1, -1, -1):
        num = i + 1
        val = 0
        for j in range(num * 2 - 1, n, num):
            # print(j)
            val += ans[j]

        val %= 2
        ans[i] = 0 if val == al[i] else 1

    c = ans.count(1)
    print(c)
    if c > 0:
        boxes = []
        for i in range(len(ans)):
            if ans[i] == 1:
                boxes.append(i + 1)
        print(' '.join(map(str, boxes)))


if __name__ == '__main__':
    main()
