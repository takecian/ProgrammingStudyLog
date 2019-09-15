# https://atcoder.jp/contests/abc141/tasks/abc141_a
import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    s = input()
    if s == 'Sunny':
        print('Cloudy')
    elif s == 'Cloudy':
        print('Rainy')
    else:
        print('Sunny')

if __name__ == '__main__':
    main()
