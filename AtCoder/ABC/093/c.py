# https://atcoder.jp/contests/abc093/tasks/arc094_a

import itertools
import collections
import bisect

def main():
    A, B, C = map(int, input().split())
    min_v = min(A, B, C)
    A -= min_v
    B -= min_v
    C -= min_v

    z = [A, B, C].count(0)
    if z == 3:
        print(0)
    elif z == 2:
        print(max(A, B, C))
    else:
        D = A if A != 0 else B
        E = C if C != 0 else B
        # print("D = {}, E = {}".format(D, E))
        count = min(D, E) // 2
        min_de = (min(D, E) // 2) * 2
        D -= min_de
        E -= min_de
        # print("{}, {}, min = {}".format(D, E, min_de))
        count += D + E
        print(count)


if __name__ == '__main__':
    main()



# 1 -> -1
# 2 -> -2