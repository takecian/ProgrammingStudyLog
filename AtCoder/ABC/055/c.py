
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    n, m = map(int, input().split())
    if n * 2 > m:
        print(m//2)
    else:
        rest = m - n * 2
        from_c_count = rest // 4
        print(n + from_c_count)

if __name__ == '__main__':
    main()
