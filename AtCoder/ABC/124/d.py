# https://atcoder.jp/contests/abc124/tasks/abc124_d

import itertools
from collections import Counter
import bisect

# 0 直立、1逆立ち
# line: 今の列、k 残り試行数
def solve(line, k):
    if all([s == '1' for s in line]):  # no need to edit
        return len(line)

    TYOKU = '0'
    SAKA = '1'

    l = 0
    r = len(line) - 1
    while l < r and k > 0:
        while l < len(line) and line[l] == SAKA:
            l += 1
        while r < len(line) and line[r] == SAKA:
            r += 1
        if line[l:r+1].count(TYOKU) > line[l:r+1].count(SAKA):
            # hanten
            for i in range(l, r+1):
                line[i] = TYOKU if line[i] == SAKA else SAKA
            print(line)
            k -= 1
        else:
            # やらないほうがいい
            l += 1
    return line.count(SAKA)


def main():
    N, K = map(int, input().split())
    S = list(input())

    # 両端の1はとる

    print(solve(S, K))


if __name__ == '__main__':
    main()
