# https://atcoder.jp/contests/abc065/tasks/abc065_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math
import heapq

def main():
    X, A, B = map(int, input().split())
    if B <= A:
        print('delicious')
        exit()
    if B <= A + X:
        print('safe')
        exit()
    print('dangerous')


if __name__ == '__main__':
    main()
