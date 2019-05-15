#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

    ans = 0
    is_valley = False
    is_mountain = False
    height = 0

    for c in s:
        if c == 'U':
            height += 1
            if height == 0:  # valley end
                ans += 1
        else:
            height -= 1
            if height == 0:  # mountain end
                pass
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
