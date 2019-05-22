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
    pass


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


