#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def solve(positions, s, t):

    if not set(t) <= set(s):
        return -1

    loop = 0
    prev_pos = -1

    for tchar in t:
        candidates = positions[tchar]
        pos = bisect.bisect_right(candidates, prev_pos)

        if pos == len(candidates):
            loop += 1
            pos = 0
        prev_pos = candidates[pos]

    return loop * len(s) + prev_pos + 1


def main():
    s = input()
    t = input()

    positions = defaultdict(list)
    for i in range(len(s)):
        positions[s[i]].append(i)

    print(solve(positions, s, t))


if __name__ == '__main__':
    main()
