import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    n, m, k  = map(int, input().split())
    if n <= min(m, k):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
