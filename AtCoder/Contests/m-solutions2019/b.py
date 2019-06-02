# https://atcoder.jp/contests/m-solutions2019/tasks/m_solutions2019_b

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    S = input()
    days = len(S)
    win = S.count('o')
    possible_win = 15 - len(S)
    print('YES' if win + possible_win >= 8 else 'NO')

if __name__ == '__main__':
    main()
