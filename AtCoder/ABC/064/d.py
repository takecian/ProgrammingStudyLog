# https://atcoder.jp/contests/abc064/tasks/abc064_d

import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math
import heapq

def main():
    N = int(input())
    S = input()

    need_left = 0
    need_right = 0
    for s in S:
        if s == '(':
            need_right += 1
        else:
            if need_right == 0:
                need_left += 1
            else:
                need_right -= 1

    ans = '(' * need_left + S + ')' * need_right
    print(ans)


if __name__ == '__main__':
    main()
