# https://atcoder.jp/contests/abc131/tasks/abc131_c

import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def main():
    A, B, C, D = map(int, input().split())

    CD = C * D // gcd(max(C, D), min(C, D))
    # A 未満で C, D で割り切れる個数
    ac_div = (A - 1) // C
    ad_div = (A - 1) // D

    acd_div = (A - 1) // CD
    a_total = ac_div + ad_div - acd_div

    # B 以下で C, D で割り切れる個数
    bc_div = B // C
    bd_div = B // D

    bcd_div = B // CD
    b_total = bc_div + bd_div - bcd_div

    # B - A から割り切れる個数を引く
    ans = B - A + 1 - (b_total - a_total)
    print(ans)


if __name__ == '__main__':
    main()
