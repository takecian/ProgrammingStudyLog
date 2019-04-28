# https://www.hackerrank.com/challenges/30-review-loop/problem

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())
    for _ in range(N):
        s = input()
        e = ''.join([s[i] for i in range(len(s)) if i % 2 == 0])
        o = ''.join([s[i] for i in range(len(s)) if i % 2 == 1])
        print("{} {}".format(e, o))

if __name__ == '__main__':
    main()
