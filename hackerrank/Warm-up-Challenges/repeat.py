# https://www.hackerrank.com/challenges/repeated-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if len(s) < n:
        one_count = s.count('a')
        repeat_count = n // len(s)
        rest = n % len(s)
        return one_count * repeat_count + s[:rest].count('a')

    else:
        return s[:n].count('a')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
