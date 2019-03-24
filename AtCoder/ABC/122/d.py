# https://atcoder.jp/contests/abc122/tasks/abc122_d

import itertools
import collections
import bisect

dp = [{} for _ in range(101)]


def is_ok(last4):
    for i in range(4):  # 全部の位置で入れ替えて確認する
        t = list(last4)
        if i >= 1:
            t[i-1], t[i] = t[i], t[i-1]
        if ''.join(t).count('AGC') > 0:
            return False
    return True


def solve(rest, lastt):
    if rest == 0:
        # print(lastt[2:])
        return 1
    if lastt in dp[rest]:
        return dp[rest][lastt]

    val = 0
    for c in 'AGCT':
        if is_ok(lastt + c):
            val += solve(rest - 1, lastt[1:] + c)
    dp[rest][lastt] = val
    return dp[rest][lastt]


def main():
    N = int(input())
    MOD = 10 ** 9 + 7
    print(solve(N, 'ZZZ') % MOD)


if __name__ == '__main__':
    main()
