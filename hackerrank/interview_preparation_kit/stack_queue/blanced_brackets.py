#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    expected = {'{':'}', '[': ']', '(': ')'}
    for c in s:
        if c == '{' or c == '[' or c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return 'NO'
            else:
                e = stack.pop()
                if expected[e] != c:
                    return 'NO'
    return 'YES' if len(stack) == 0 else 'NO'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
