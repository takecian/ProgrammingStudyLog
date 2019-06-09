# https://atcoder.jp/contests/abc129/tasks/abc129_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    P, Q, R = map(int, input().split())
    print(min(P + Q, Q + R, R + P))

if __name__ == '__main__':
    main()
