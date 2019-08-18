#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    a = int(input())
    s = input()
    print(s if a >= 3200 else 'red')

if __name__ == '__main__':
    main()
