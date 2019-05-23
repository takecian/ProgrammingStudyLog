# https://atcoder.jp/contests/abc064/tasks/abc064_b

import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math
import heapq

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A) - min(A))

if __name__ == '__main__':
    main()
