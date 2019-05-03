# https://www.hackerrank.com/challenges/30-binary-numbers/problem

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    n = int(input())
    bin = "{0:b}".format(n).split('0')
    # print(bin)
    l = map(lambda s: len(s), bin)
    # print(list(l))
    print(max(l))

if __name__ == '__main__':
    main()
