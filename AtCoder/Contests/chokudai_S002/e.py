#

import itertools
import collections
import bisect

def main():
    N = int(input())
    ans = 0
    for _ in range(N):
        a, b = map(int, input().split())
        ans += min(a//2, b)
    print(ans)


if __name__ == '__main__':
    main()
