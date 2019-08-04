#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    s = input()
    ans = []

    def create(l, r):
        left = [0] * (r - 1)
        right = [0] * (l - 1)
        total = r + l
        if total % 2 == 0:
            return left + [total // 2, total // 2] + right
        else:
            step = max(l, r) - 1
            if step % 2 == 0:
                if r > l:
                    return left + [total // 2 + 1, total // 2] + right
                else:
                    return left + [total // 2, total // 2 + 1] + right
            else:
                if r > l:
                    return left + [total // 2, total // 2 + 1] + right
                else:
                    return left + [total // 2 + 1, total // 2] + right
    r = 0
    l = 0
    for c in s:
        if c == 'R':
            if l > 0:
                ans += create(l, r)
                r = 0
                l = 0
            r += 1
        else:
            l += 1

    if l > 0:
        ans += create(l, r)
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
