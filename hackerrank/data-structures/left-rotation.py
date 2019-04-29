# https://www.hackerrank.com/challenges/array-left-rotation/problem

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    n, d  = map(int, input().split())
    a = list(map(int, input().split()))
    r = a[d:] + a[0:d]
    print(' '.join(map(str, r)))

if __name__ == '__main__':
    main()
