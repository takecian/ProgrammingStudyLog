# https://www.hackerrank.com/challenges/30-conditional-statements/problem

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())
    if N % 2 == 1 or 5 < N < 21:
        print("Weird")
    else:
        print("Not Weird")

if __name__ == '__main__':
    main()
