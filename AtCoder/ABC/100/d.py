# https://abc100.contest.atcoder.jp/tasks/abc100_d
# NOTE: TLE

import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def calc1(tup):
    return tup[0] + tup[1] + tup[2]

def calc2(tup):
    return tup[0] + tup[1] - tup[2]

def calc3(tup):
    return tup[0] - tup[1] + tup[2]

def calc4(tup):
    return tup[0] - tup[1] - tup[2]

def calc5(tup):
    return -tup[0] + tup[1] + tup[2]

def calc6(tup):
    return -tup[0] + tup[1] - tup[2]

def calc7(tup):
    return -tup[0] - tup[1] + tup[2]

def calc8(tup):
    return -tup[0] - tup[1] - tup[2]
def calc1(tup):
    return tup[0] + tup[1] + tup[2]

def calc2(tup):
    return tup[0] + tup[1] - tup[2]

def calc3(tup):
    return tup[0] - tup[1] + tup[2]

def calc4(tup):
    return tup[0] - tup[1] - tup[2]

def calc5(tup):
    return -tup[0] + tup[1] + tup[2]

def calc6(tup):
    return -tup[0] + tup[1] - tup[2]

def calc7(tup):
    return -tup[0] - tup[1] + tup[2]

def calc8(tup):
    return -tup[0] - tup[1] - tup[2]


def main():
    n, m = map(int, input().split())
    xyzl = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        xyzl.append((x,y,z))

    ans = 0
    xyzl.sort(key=lambda xyz: -calc1(xyz))
    ans = max(ans, sum([calc1(xyz) for xyz in xyzl[:m]]))
    xyzl.sort(key=lambda xyz: -calc2(xyz))
    ans = max(ans, sum([calc2(xyz) for xyz in xyzl[:m]]))
    xyzl.sort(key=lambda xyz: -calc3(xyz))
    ans = max(ans, sum([calc3(xyz) for xyz in xyzl[:m]]))
    xyzl.sort(key=lambda xyz: -calc4(xyz))
    ans = max(ans, sum([calc4(xyz) for xyz in xyzl[:m]]))

    xyzl.sort(key=lambda xyz: -calc5(xyz))
    ans = max(ans, sum([calc5(xyz) for xyz in xyzl[:m]]))
    xyzl.sort(key=lambda xyz: -calc6(xyz))
    ans = max(ans, sum([calc6(xyz) for xyz in xyzl[:m]]))
    xyzl.sort(key=lambda xyz: -calc7(xyz))
    ans = max(ans, sum([calc7(xyz) for xyz in xyzl[:m]]))
    xyzl.sort(key=lambda xyz: -calc8(xyz))
    ans = max(ans, sum([calc8(xyz) for xyz in xyzl[:m]]))

    print(ans)


if __name__ == '__main__':
    main()

