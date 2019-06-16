#

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def reverse_insort(a, x, lo=0, hi=None):
    """Insert item x in list a, and keep it reverse-sorted assuming a
    is reverse-sorted.

    If x is already in a, insert it to the right of the rightmost x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x > a[mid]: hi = mid
        else: lo = mid+1
    a.insert(lo, x)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    index = bisect.bisect_left(A, 0)
    minus = A[:index]
    minus.reverse()
    plus = A[index:]
    # print(minus)
    # print(plus)
    progres = []
    ans = 0
    while True:
        if len(plus) == 1 and len(minus) == 1:
            p = plus.pop()
            m = minus.pop()
            progres.append((p, m))
            ans = p - m
            # print('{} {}'.format(p, m))
            break

        if len(plus) == 1 and len(minus) == 0:
            ans = plus.pop()
            break
        if len(plus) == 0 and len(minus) == 1:
            ans = minus.pop()
            break

        # まだ2つ以上入ってる
        if len(plus) == 0:
            val1 = minus.pop()  # 一番小さい
            val2 = minus.pop(0)
            new_val = val2 - val1
            plus.append(new_val)
            progres.append((val2, val1))
            # print('{} {}'.format(val1, val2))
            continue
        if len(minus) == 0:
            val1 = plus.pop(0)
            val2 = plus.pop()
            new_val = val1 - val2
            minus.append(new_val)
            progres.append((val1, val2))
            # print('{} {}'.format(val2, val1))
            continue

        if len(plus) > len(minus):
            val1 = plus.pop()
            val2 = minus.pop()
            new_val = val2 - val1
            reverse_insort(minus, new_val)
            progres.append((val2, val1))
            # print('{} {}'.format(val2, val1))
        else:
            val1 = plus.pop()
            val2 = minus.pop()
            new_val = val1 - val2
            index = bisect.bisect_left(plus, new_val)
            plus.insert(index, new_val)
            progres.append((val1, val2))
            # print('{} {}'.format(val1, val2))

    print(ans)
    for p, q in progres:
        print('{} {}'.format(p, q))


if __name__ == '__main__':
    main()
