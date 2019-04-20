# https://tenka1-2018-beginner.contest.atcoder.jp/tasks/tenka1_2018_b

import itertools
from collections import Counter
import bisect

def main():
    A, B, K = map(int, input().split())
    for i in range(1, K+1):
        if i % 2 == 1:
            A -= A % 2
            A, B = A // 2, B + A // 2
        else:
            B -= B % 2
            B, A = B // 2, A + B // 2
    print("{} {}".format(A, B))

if __name__ == '__main__':
    main()
