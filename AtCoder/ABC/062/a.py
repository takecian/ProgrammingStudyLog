
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    x, y = map(int, input().split())
    group_a = [1,3,5,7,8,10,12]
    group_b = [4,6,9,11]
    group_c = [2]
    if x in group_a and y in group_a:
        print('Yes')
        return
    if x in group_b and y in group_b:
        print('Yes')
        return
    if x in group_c and y in group_c:
        print('Yes')
        return
    print('No')


if __name__ == '__main__':
    main()
