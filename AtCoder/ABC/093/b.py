# https://atcoder.jp/contests/abc093/tasks/abc093_b

import itertools
import collections
import bisect

def main():
    A, B, K = map(int, input().split())
    ans = []
    for i in range(K):
        if A <= A + i <= B:
            ans.append(A + i)
        else:
            break
    for i in range(K):
        if A <= B - i <= B :
            ans.append(B - i)
        else:
            break

    # print(ans)
    ans = list(set(ans))
    ans.sort()
    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
