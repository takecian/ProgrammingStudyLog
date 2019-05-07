# https://atcoder.jp/contests/cpsco2019-s3/tasks/cpsco2019_s3_b

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    i = 0
    while M > 0:
        M -= A[i]
        i += 1
    print(i)


if __name__ == '__main__':
    main()
