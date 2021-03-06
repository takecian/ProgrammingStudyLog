# https://atcoder.jp/contests/abc122/tasks/abc122_c

import itertools
import collections
import bisect

def main():
    N, Q = map(int, input().split())
    S = list(input())

    counter = [0] * N
    for i in range(N-1):
        if "{}{}".format(S[i], S[i+1]) == 'AC':
            counter[i] = 1 + (counter[i - 1] if i > 0 else 0)
        else:
            counter[i] = counter[i - 1] if i > 0 else 0
    # print(counter)

    for _ in range(Q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        print(counter[r - 1] - counter[l - 1])

if __name__ == '__main__':
    main()
