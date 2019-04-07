# https://atcoder.jp/contests/abc123/tasks/abc123_b

import itertools
import collections
import bisect

def main():
    # big value
    INF = int(1e15)
    last = INF
    menus = []
    for _ in range(5):
        m = int(input())
        if last == INF:
            last = m
        else:
            if m % 10 != 0:
                m_d = m % 10
                l_d = last % 10
                if m_d < l_d:
                    last = m
        menus.append(m)

    ans = 0
    last_done = False
    for m in menus:
        if m == last and not last_done:
            ans += m
            last_done = True
        else:
            if m % 10 == 0:
                ans += m
            else:
                ans += m + (10 - m % 10)
    print(ans)


if __name__ == '__main__':
    main()
