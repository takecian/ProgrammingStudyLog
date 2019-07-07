# https://atcoder.jp/contests/abc133/tasks/abc133_c

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    l, r = map(int, input().split())

    l_i = l // 2019
    r_i = r // 2019
    if l_i != r_i:
        print(0)
    else:
        ans = l * r % 2019
        for x in range(l, r):
            for y in range(l + 1, r + 1):
                ans = min(ans, x * y % 2019)
        print(ans)


if __name__ == '__main__':
    main()
