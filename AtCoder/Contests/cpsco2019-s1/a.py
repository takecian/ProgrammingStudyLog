# https://atcoder.jp/contests/cpsco2019-s1/tasks/cpsco2019_s1_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math

def main():
    N, A = map(int, input().split())
    mi = min(N // 3, math.ceil(A / 3))
    ma = min(N // 3, A)
    print('{} {}'.format(mi, ma))

if __name__ == '__main__':
    main()
