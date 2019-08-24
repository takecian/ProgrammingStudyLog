# https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_a

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    m, d = map(int, input().split())
    ans = 0
    for i in range(1, m + 1):
        for j in range(10, d + 1):
            d1 = int(str(j)[1])
            d10 = int(str(j)[0])
            if d1 < 2 or d10 < 2:
                continue
            if i == d1 * d10:
                # print('{} {} {}'.format(i, d10, d1))
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
