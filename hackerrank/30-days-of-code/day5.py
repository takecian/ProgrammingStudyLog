# https://www.hackerrank.com/challenges/30-loops/problem

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())
    for i in range(10):
        print("{} x {} = {}".format(N, i + 1, N * (i + 1)))

if __name__ == '__main__':
    main()
