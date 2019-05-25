# https://atcoder.jp/contests/abc127/tasks/abc127_b

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    r, D, X = map(int, input().split())
    xi = X
    for i in range(1, 11):
        xi = r * xi - D
        print(xi)

if __name__ == '__main__':
    main()
