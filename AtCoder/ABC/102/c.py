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
    for i in range(n):
        al[i] = al[i] - (i + 1)
    al.sort()

    b = al[(n-1)//2]
    ans = sum([abs(a - b) for a in al])
    print(ans)

if __name__ == '__main__':
    main()
