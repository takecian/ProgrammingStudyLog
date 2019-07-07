#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 山1 に降った雨を計算する
    m1 = a[0] * 2
    for i in range(1, n):
        if i % 2 == 1:
            m1 = m1 - a[i] * 2
        else:
            m1 = m1 + a[i] * 2
    m1 //= 2
    # print(m1)

    ans = [m1]
    for i in range(n-1):
        rest = a[i] - ans[-1] // 2
        ans.append(rest * 2)
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
