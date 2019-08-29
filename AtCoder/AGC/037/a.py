# https://atcoder.jp/contests/agc037/tasks/agc037_a
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

    k = 1
    i = 1
    prev = s[0]
    while i < len(s):
        if prev != s[i]:
            prev = s[i]
            k += 1
            i += 1
        else:
            two = s[i:(i+2)]
            if len(two) == 2:
                prev = two
                k += 1
                i += 2
            else:
                break

        # print('{} {}, {}'.format(prev, k, i))
    print(k)


if __name__ == '__main__':
    main()
