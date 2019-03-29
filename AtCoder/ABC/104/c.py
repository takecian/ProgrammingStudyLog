# https://atcoder.jp/contests/abc104/tasks/abc104_c

import itertools
import collections
import bisect
import math

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for _ in range(D):
        pi, ci  = map(int, input().split())
        p.append(pi)
        c.append(ci)


    # big value
    INF = int(1e15)
    ans = INF
    # Bit 全探索
    pattern = 1 << D  # 1 をリストの長さだけ左にシフトする
    for i in range(pattern):
        scope = []
        for j in range(D):
            if (i >> j) & 1:
                scope.append(j)

        score = 0
        result = 0
        for s in scope:
            score += (s + 1) * p[s] * 100 + c[s]
            result += p[s]

        # print("i = {}, score = {}, result = {}".format(i, score, result))
        if score < G:
            for idx in range(D - 1, -1, -1):
                if idx not in scope:
                    rest = G - score
                    count = min(math.ceil(rest / ((idx + 1) * 100)), p[idx])
                    # print("idx = {}, count = {}".format(idx, count))
                    score += (idx + 1) * count * 100
                    result += count
                    break

        # print("i = {}, score = {}, result = {}".format(i, score, result))
        if score >= G:
            ans = min(ans, result)

    print(ans)


if __name__ == '__main__':
    main()
