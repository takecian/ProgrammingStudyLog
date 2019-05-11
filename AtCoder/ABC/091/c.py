# https://atcoder.jp/contests/abc091/tasks/arc092_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())
    red = [list(map(int, input().split())) for _ in range(N)]
    red.sort(key=lambda x: x[0])

    blue = [list(map(int, input().split())) for _ in range(N)]
    blue.sort(key=lambda x: x[0])

    ans = 0
    for bx, by in blue:
        p_red = None
        for i in range(len(red)):
            rx, ry = red[i][0], red[i][1]
            if rx > bx:
                break
            if ry < by:
                if not p_red:
                    p_red = red[i]
                else:
                    if p_red[1] < ry:
                        p_red = red[i]
        if p_red:
            ans += 1
            red.remove(p_red)

    print(ans)

if __name__ == '__main__':
    main()
