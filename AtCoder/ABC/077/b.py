# https://atcoder.jp/contests/abc077/tasks/abc077_b

import itertools
import collections
import bisect

def main():
    N = int(input())

    ans =1
    i = 1
    while N >= i * i:
        ans = i * i
        i += 1
    print(ans)

if __name__ == '__main__':
    main()
