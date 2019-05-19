# https://www.hackerrank.com/challenges/30-nested-logic/problem

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def calc():
    a_d, a_m, a_y = map(int, input().split())
    e_d, e_m, e_y = map(int, input().split())
    if a_y < e_y or (a_m < e_m and a_y == e_y) or (a_d < e_d and a_m == e_m and a_y == e_y):
        return 0
    if a_m == e_m and a_y == e_y:
        return 15 * (a_d - e_d)
    if a_y == e_y:
        return 500 * (a_m - e_m)
    return 10000

def main():
    print(calc())


if __name__ == '__main__':
    main()
