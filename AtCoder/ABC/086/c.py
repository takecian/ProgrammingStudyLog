# https://atcoder.jp/contests/abc081/tasks/arc086_a

import itertools
import collections
import bisect

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    C = collections.Counter(A)
    need_rewrite = max(0, len(C.keys()) - K)
    if need_rewrite:
        ans = 0
        for kv in C.most_common()[-need_rewrite:]:
            ans += kv[1]
        print(ans)
    else:
        print(0)


if __name__ == '__main__':
    main()
