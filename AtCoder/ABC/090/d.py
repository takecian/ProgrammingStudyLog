# https://atcoder.jp/contests/abc090/tasks/arc091_b

import itertools
import collections
import bisect


def main():
    N, K = map(int, input().split())
    ans = 0
    for b in range(K+1, N+1):
        p = N // b
        r = N - b * p

        rest = max(0, r - K + 1) if K != 0 else max(0, r - K)
        tmp_ans = p * (b - K) + rest  # 該当する部分をまとめて計算する
        # print("b = {}, c = {}, p = {}, tmp = {}".format(b, b - K, p, tmp))
        ans += tmp_ans

    print(ans)


if __name__ == '__main__':
    main()
