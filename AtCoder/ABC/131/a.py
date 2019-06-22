#

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    s = list(input())
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        print('Bad')
    else:
        print('Good')


if __name__ == '__main__':
    main()
