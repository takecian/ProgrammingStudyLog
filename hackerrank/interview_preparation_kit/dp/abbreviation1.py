#!/bin/python3

import math
import os
import random
import re
import sys
import re

# Complete the abbreviation function below.
memo = {}
def solve(a, b):
    # print('input: a = {}, b = {}'.format(a, b))
    key = '{}#{}'.format(a, b)
    if key in memo:
        return memo[key]

    if a.upper() == b:
        memo[key] = True
        return True

    only_capitals = re.sub('[a-z]', '', a)
    if only_capitals == b:
        memo[key] = True
        return True

    if len(a) == 0 or len(b) == 0 or len(a) < len(b):
        # print('a = {}, b = {}, impossible'.format(a, b))
        memo[key] = False
        return False

    if a[0].isupper():
        if a[0] == b[0]:
            memo[key] = solve(a[1:], b[1:])
        else:
            # print('a = {}, b = {}, impossible'.format(a, b))
            memo[key] = False
    else:  # lower
        if a[0].upper() == b[0]:
            # print('1a = {}, b = {}'.format(a, b))
            memo[key] = solve(a[1:], b[1:]) or solve(a[1:], b)
        else:
            # print('2a = {}, b = {}'.format(a, b))
            memo[key] = solve(a[1:], b)
    return memo[key]


def abbreviation(a, b):
    global memo
    memo = {}
    if solve(a, b):
        return 'YES'
    else:
        return 'NO'

def main():
    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        print(result)

if __name__ == '__main__':
    main()


