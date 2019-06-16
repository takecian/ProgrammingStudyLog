# https://atcoder.jp/contests/abc130/tasks/abc130_c
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    W, H, x, y = map(int, input().split())
    area = W * H
    if x == W / 2 and y == H / 2:  # 中点
        print('{} {}'.format(area / 2, 1))
    else:
        print('{} {}'.format(area / 2, 0))


if __name__ == '__main__':
    main()
