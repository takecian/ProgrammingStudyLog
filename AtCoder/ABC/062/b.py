# https://atcoder.jp/contests/abc062/tasks/abc062_b

import itertools
import collections
import bisect

def main():
    H, W = map(int, input().split())
    lines = [input() for _ in range(H)]
    sharp = '#' * (W + 2)

    print(sharp)
    for line in lines:
        print('#{}#'.format(line))

    print(sharp)


if __name__ == '__main__':
    main()
