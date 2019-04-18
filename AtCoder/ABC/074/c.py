# https://atcoder.jp/contests/abc074/tasks/arc083_a

import itertools
from collections import Counter
import bisect

def main():
    A, B, C, D, E, F = map(int, input().split())

    ans_nod = -1
    ans_sugar = 0
    ans_water = 0
    for a in range(31):
        for b in range(31):
            water = a * A * 100 + b * B * 100
            if water == 0:
                continue
            if water > F:
                continue
            max_sugar = E * (a * A + b * B)
            for i in range(3000):
                for j in range(3000):
                    sugar = i * C + j * D
                    if sugar > max_sugar:  # 解けないならダメ
                        break
                    if sugar + water > F:  # F超えるならダメ
                        break
                    nod = 100 * sugar / (water + sugar)
                    if nod > ans_nod:
                        ans_nod = nod
                        ans_sugar = sugar
                        ans_water = water
    print("{} {}".format(ans_water + ans_sugar, ans_sugar))


if __name__ == '__main__':
    main()
