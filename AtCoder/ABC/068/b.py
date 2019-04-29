# https://atcoder.jp/contests/abc068/tasks/abc068_b

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())
    ans = 0
    count = -1
    for i in range(1, N+1):
        c = 0
        v = i
        while v % 2 == 0:
            c += 1
            v //= 2
        if c > count:
            count = c
            ans = i

    print(ans)


if __name__ == '__main__':
    main()
