# https://www.hackerrank.com/challenges/30-bitwise-and/problem

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        if k % 2 == 0:
            print(k - 2)
        else:
            print(k - 1)

