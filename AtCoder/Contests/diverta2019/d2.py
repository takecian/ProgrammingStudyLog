# https://atcoder.jp/contests/diverta2019/tasks/diverta2019_d
import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())

    ans = 0
    for i in range(1, N):
        l = 1
        r = N
        while l < r:
            m = (l + r) // 2
            div = N // m
            div2 = N // (m + 1)
            div3 = N // (m - 1)
            if div >= i:
                if div2 >= i: # 大きい
                    l = m + 1
                else:
                    r = m
            else:
                if div3 < i:
                    r = m - 1
                else:
                    l = m
            # print('l = {}, r = {}'.format(l, r))

        m = (l + r) // 2
        print('i = {}, m = {}'.format(i, m))

    # end = m
    #
    # print('start {}, end {}'.format(start, end))

    ans = 0
    # for i in range(start, end + 1):
    #     if N // i == N % i:
    #         ans += i
    #
    # ans += (N - 1)

    print(ans)


if __name__ == '__main__':
    main()
