# https://atcoder.jp/contests/abc107/tasks/arc101_a

import itertools
import collections
import bisect

def main():
    # big value
    INF = int(1e15)

    N, K = map(int, input().split())
    X = [-INF] + list(map(int, input().split())) + [INF]
    pos = bisect.bisect(X, 0) # 0より大きい中で最小の要素のインデックス
    # print(pos)

    right_num = N - pos + 1
    left_num = pos - 1

    ans = INF
    if right_num >= K:  # 右側からだけ取れるなら
        ans = min(ans, abs(X[pos + K - 1]))
    # print(ans)

    for i in range(1, K):  # 左側からいくつ取るか
        if i > left_num:  # 左側に取れるだけ数がないなら continue
            continue
        if K - i > right_num:  # 右側に取れるだけ数がないなら continue
            continue

        left_distance = abs(X[pos - i])
        right_distance = abs(X[pos + K - i - 1])
        # min(一番左までの距離 x 往復 + 一番右までの距離, 一番右までの距離 x 往復 + 一番左までの距離)
        ans = min(ans, left_distance * 2 + right_distance, right_distance * 2 + left_distance)

    if left_num >= K:  # 左側からだけ取れるなら
        ans = min(ans, abs(X[pos - K]))
    # print(ans)

    print(ans)


if __name__ == '__main__':
    main()
