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
    for _ in range(len(n)):
        x, y, z = map(int, input().split())
        xyzl.append((x,y,z))



if __name__ == '__main__':
    main()

