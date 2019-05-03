# https://atcoder.jp/contests/iroha2019-day1/tasks/iroha2019_day1_h

import itertools
from collections import Counter
from collections import defaultdict
import bisect


def conv(n):
    return sum(map(int, list(str(n))))


def main():
    N = int(input())
    v = conv(N)
    rev = list(map(int, list(str(N))))
    rev = rev[::-1]

    # print(rev)
    ans = []
    while v > 0:
        if v > 9:
            ans.append(9)
            v -= 9
        else:
            ans.append(v)
            v -= v

    ans.reverse()
    # print(ans)
    val = int(''.join(map(str, ans)))

    if val == N:
        if val < 10:
            val = val + 9
        else:
            i = ans.index(9)
            val = val + 10 ** (len(ans) - i - 1) * 9


    print(val)


if __name__ == '__main__':
    main()
