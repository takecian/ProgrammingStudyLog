# https://atcoder.jp/contests/abc127/tasks/abc127_e

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    MOD = 10**9 + 7
    N, M, K = map(int, input().split())

    ans = 0
    for l in list(itertools.combinations(range(N*M), K)):
        for i in range(len(l)-1):
            iy = l[i] // M
            ix = l[i] % M
            for j in range(i + 1, len(l)):
                jy = l[j] // M
                jx = l[j] % M
                ans += abs(iy - jy) + abs(ix - jx)
                ans = ans % MOD

    print(ans)



if __name__ == '__main__':
    main()
