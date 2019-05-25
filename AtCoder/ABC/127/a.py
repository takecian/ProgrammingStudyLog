#

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    else:
        if 6 <= A <= 12:
            print(B // 2)
        else:
            print(0)

if __name__ == '__main__':
    main()
