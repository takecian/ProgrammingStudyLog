# https://atcoder.jp/contests/abc090/tasks/abc090_b

import itertools
import collections
import bisect

def main():
    A, B = map(int, input().split())
    ans = 0
    for i in range(A, B+1):
        j = int(str(i)[::-1])
        if i == j:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
