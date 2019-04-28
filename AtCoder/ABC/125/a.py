#

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    A, B, T = map(int, input().split())
    print(T // A * B)

if __name__ == '__main__':
    main()
