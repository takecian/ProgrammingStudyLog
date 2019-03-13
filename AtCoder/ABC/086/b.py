# https://atcoder.jp/contests/abc086/tasks/abc086_b

import itertools
import collections
import bisect
import math

def main():
    a, b = map(int, input().split())
    val = int("{}{}".format(a, b))

    print("Yes" if math.sqrt(val).is_integer() else "No")

if __name__ == '__main__':
    main()
