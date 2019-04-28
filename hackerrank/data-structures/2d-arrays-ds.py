import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    arr = [list(map(int, input().split())) for _ in range(6)]

    # big value
    INF = int(1e15)
    ans = -INF
    for h in range(1, 5):
        for w in range(1, 5):
            center = (h, w)

            s = 0
            dhs = [-1, -1, -1, 0,  1, 1, 1]
            dws = [-1,  0,  1, 0, -1, 0, 1]
            for dh, dw in zip(dhs, dws):
                s += arr[center[0] + dh][center[1] + dw]
            # print("{}, sum = {}".format(center, s))
            ans = max(ans, s)

    print(ans)


if __name__ == '__main__':
    main()


# -9 -9 -9  1 1 1
#  0 -9  0  4 3 2
# -9 -9 -9  1 2 3
#  0  0  8  6 6 0
#  0  0  0 -2 0 0
#  0  0  1  2 4 0
