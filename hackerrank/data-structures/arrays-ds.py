# https://www.hackerrank.com/challenges/arrays-ds/problem

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    print(' '.join(map(str, A)))

if __name__ == '__main__':
    main()
