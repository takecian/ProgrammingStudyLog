import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    s = input()
    multis = s.split('+')

    ans = 0
    for exp in multis:
        if len(exp) == 0 and exp != '0':
            ans += 1
        else:
            tokens = exp.split('*')
            zero_include = False
            for token in tokens:
                if token == '0':
                    zero_include = True
                    break
            if not zero_include:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
