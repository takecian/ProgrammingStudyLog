#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    cursor = 0
    for i in range(len(a)):
        if b[cursor] == a[i]:
            cursor += 1
        if cursor == len(b):
            return 'YES'
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


