# https://atcoder.jp/contests/diverta2019/tasks/diverta2019_a
import itertools
from collections import Counter
from collections import defaultdict
import bisect


def main():
    N, K = map(int, input().split())
    print(N - K + 1)

if __name__ == '__main__':
    main()
