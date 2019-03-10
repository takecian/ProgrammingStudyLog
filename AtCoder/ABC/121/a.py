# https://atcoder.jp/contests/abc121/tasks/abc121_a
import itertools
import collections
import bisect

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print((H-h)*(W-w))


if __name__ == '__main__':
    main()
