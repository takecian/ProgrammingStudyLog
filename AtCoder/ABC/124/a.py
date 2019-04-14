#

import itertools
from collections import Counter
import bisect

def main():
    A, B = map(int, input().split())
    print(max(A + B, A + A - 1, B + B - 1))

if __name__ == '__main__':
    main()
