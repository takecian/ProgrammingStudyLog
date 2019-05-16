# https://www.hackerrank.com/challenges/max-array-sum/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    length = len(arr) + 2
    dp = [0] * length
    for i in range(2, length):
        print(i)
        dp[i] = max(dp[i-1], dp[i-2], dp[i-2] + arr[i-2])

    return max(dp[-2], dp[-1])


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    print(res)