# https://atcoder.jp/contests/iroha2019-day1/tasks/iroha2019_day1_e
import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N, A, B = map(int, input().split())
    D = []
    if B != 0:
        D = list(map(int, input().split()))

    if A == 1:
        print(0)
        exit()

    D.sort()
    D.insert(0, 0)
    D.append(N + 1)

    diff = []
    for i in range(1, len(D)):
        di = D[i] - D[i-1]
        diff.append(di)
    # print(diff)

    dates = 0
    for di in diff:
        dates += (di - 1) // A
    print(N - (dates + B))


if __name__ == '__main__':
    main()
