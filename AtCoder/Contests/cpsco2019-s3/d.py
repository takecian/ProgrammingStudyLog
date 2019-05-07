# https://atcoder.jp/contests/cpsco2019-s3/tasks/cpsco2019_s3_d

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())
    S = list(input())
    expect = ['R']

    if S[0] != 'R' or S[-1] != 'B':
        print('No')
        exit()

    for s in S:
        if s in expect:
            if s == 'R':
                expect = ['R', 'G']
            elif s == 'G':
                expect = ['R', 'B']
            else:  # B
                expect = ['R', 'G', 'B']
        else:
            print('No')
            exit()


    print('Yes')


if __name__ == '__main__':
    main()
