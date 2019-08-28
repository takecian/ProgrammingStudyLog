#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    a, k = map(int, input().split())
    cho = 2 * 10 ** 12

    if k == 0:
        print(cho - a)
        return

    day = 0
    while a < cho:
        a = a + 1 + a * k
        day += 1

    print(day)


if __name__ == '__main__':
    main()
