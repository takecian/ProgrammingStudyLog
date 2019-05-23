# https://atcoder.jp/contests/abc066/tasks/abc066_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    rings = list(map(int, input().split()))
    print(sum(rings) - max(rings))

if __name__ == '__main__':
    main()
