#

import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


# コピペしてきた、ちゃんと理解してないのでまた調べる
def f(N):
    win = 1

    left = N + 1
    result = win

    while True:
        if left == 1:
            break
        x = left // 2
        right = left - 1
        if left % 2 == 0:
            left = x
        else:
            # xだと選べる
            if result == win:
                left = x + 1
            else:
                left = x
        result = 1 - result
        continue

    answer = 'Takahashi' if result == win else 'Aoki'
    print(answer)


def main():
    n = int(input())

    f(n)


if __name__ == '__main__':
    main()
