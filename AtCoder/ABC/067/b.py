# https://atcoder.jp/contests/abc067/tasks/abc067_b

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N, K = map(int, input().split())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    print(sum(L[:K]))

if __name__ == '__main__':
    main()
