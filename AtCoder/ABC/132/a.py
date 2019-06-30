#
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    s = list(input())
    s.sort()
    if s[0] == s[1] and s[2] == s[3] and s[0] != s[2]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
