#
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    m1 = d[n//2 - 1]
    m2 = d[n//2]
    # print('{} {}'.format(m1, m2))
    if m1 == m2:
        print(0)
    else:
        ans = m2 - m1
        print(ans)

if __name__ == '__main__':
    main()
