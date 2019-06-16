#
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    X, A = map(int, input().split())
    print(0 if X < A else 10)

if __name__ == '__main__':
    main()
