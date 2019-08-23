# https://atcoder.jp/contests/abc045/tasks/arc061_a
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

    def build(sub):
        if len(sub) == 1:
            return [sub]
        top = sub[0]
        rest = build(sub[1:])

        ret = []
        for r in rest:
            ret.append(top + r)
            ret.append(top + '+' + r)
        return ret

    ans = sum(map(lambda inp: eval(inp), build(s)))
    print(ans)


if __name__ == '__main__':
    main()
