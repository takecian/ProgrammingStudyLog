# https://atcoder.jp/contests/abc128/tasks/abc128_d

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N, K = map(int, input().split())
    D = list(map(int, input().split()))

    ans = 0
    try_count = min(N, K)
    for a in range(try_count + 1):
        # print(a)
        b = 0
        while b <= try_count - a:
            can_discard = K - a - b
            # print('{} {} {}'.format(a, b, can_discard))
            gets = D[:a] + D[N - b:]
            # print(gets)
            gets.sort()

            while len(gets) > 0 and can_discard > 0:
                if gets[0] < 0:
                    gets.pop(0)
                    can_discard -= 1
                else:
                    break

            # print(gets)
            ans = max(ans, sum(gets))
            b += 1

    print(ans)


if __name__ == '__main__':
    main()
