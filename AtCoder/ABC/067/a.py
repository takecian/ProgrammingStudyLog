# https://atcoder.jp/contests/abc067/tasks/abc067_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    A, B = map(int, input().split())
    if A % 3 == 0 or B % 3 == 0 or (A + B) % 3 == 0:
        print('Possible')
    else:
        print('Impossible')


if __name__ == '__main__':
    main()
