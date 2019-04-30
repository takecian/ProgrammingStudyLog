# https://atcoder.jp/contests/iroha2019-day1/tasks/iroha2019_day1_b
import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    S = input()
    K = int(input())
    for _ in range(K):
        S = S[1:] + S[0]
    print(S)


if __name__ == '__main__':
    main()
