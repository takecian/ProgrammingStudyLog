# https://atcoder.jp/contests/agc030/tasks/agc030_b

import itertools
import collections
import bisect

def main():
    L, N = map(int, input().split())
    X = [int(input()) for _ in range(N)]
    dist = 0
    pos = 0
    l = 0
    r = N - 1
    while l <= r:
        dis_l = abs((X[l] - pos + L) % L)
        dis_r = abs((pos + L - X[r]) % L)
        print("l dis = {}, r dis = {}, pos = {}".format(dis_l, dis_r, pos))
        if dis_l < dis_r:
            dist += dis_r
            pos = X[r]
            r -= 1
        else:
            dist += dis_l
            pos = X[l]
            l += 1

    print(dist)


if __name__ == '__main__':
    main()
