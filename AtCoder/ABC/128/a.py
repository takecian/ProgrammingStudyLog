#

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    A, P = map(int, input().split())
    print((A * 3 + P) // 2)

if __name__ == '__main__':
    main()
