# https://atcoder.jp/contests/abc128/tasks/abc128_c

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N, M = map(int, input().split())

    S = []
    for _ in range(M):
        ks = list(map(int, input().split()))
        S.append(ks[1:])

    P = list(map(int, input().split()))

    # print(S)
    # print(P)

    ans = 0
    # Bit 全探索
    pattern = 1 << N
    for i in range(pattern):
        scope = []
        for j in range(N):
            if (i >> j) & 1:
                scope.append(j + 1)

        if len(scope) > 0:
            turn_on = True
            for j in range(len(S)):
                switches = S[j]
                c = 0
                for states in scope:
                    if states in switches:
                        c += 1
                if c % 2 != P[j]:
                    turn_on = False
                if not turn_on:
                    break
            if turn_on:
                # print('ok = {}'.format(scope))
                ans += 1
        else:
            turn_on = True
            for j in range(len(S)):
                if P[j] != 0:
                    turn_on = False
            if turn_on:
                ans += 1


    print(ans)


if __name__ == '__main__':
    main()
