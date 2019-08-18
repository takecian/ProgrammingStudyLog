#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n = int(input())
    al = list(map(int, input().split()))
    su = sum([1/a for a in al])
    print(1/su)

if __name__ == '__main__':
    main()
