# https://tenka1-2019-beginner.contest.atcoder.jp/tasks/tenka1_2019_d

import itertools
from collections import Counter
import bisect

MOD = 998244353
# R+G>B  かつ G+B>R かつ B+R>G

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    print(A)

if __name__ == '__main__':
    main()
