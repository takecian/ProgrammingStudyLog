#

import itertools
from collections import Counter
import bisect

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 1
    prev = 0
    for i in range(1, N):
        can_see = True
        for j in range(0, i):
            if H[j] > H[i]:
                can_see = False
        if can_see:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
