# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    ans = 0

    position = 0
    while position < len(c) - 1:
        step1 = min(len(c) - 1, position + 1)
        step2 = min(len(c) - 1, position + 2)
        if c[step2] == 0:
            position = step2
            ans += 1
        else:
            position = step1
            ans += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
