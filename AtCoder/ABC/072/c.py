# https://atcoder.jp/contests/abc072/tasks/arc082_a

import itertools
import collections
import bisect

def main():
    N = int(input())
    A = list(map(int, input().split()))

    c = collections.Counter()
    for a in A:
        c[a-1] += 1
        c[a] += 1
        c[a+1] += 1
    print(c.most_common()[0][1])


if __name__ == '__main__':
    main()
