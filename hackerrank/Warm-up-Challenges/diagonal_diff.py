# https://www.hackerrank.com/challenges/diagonal-difference/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    ltor_sum = 0
    rtol_sum = 0
    for i in range(len(arr)):
        ltor_sum += arr[i][i]
        rtol_sum += arr[i][len(arr) - 1 - i]

    return abs(ltor_sum - rtol_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
