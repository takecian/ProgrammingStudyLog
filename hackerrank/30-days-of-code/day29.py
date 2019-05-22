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

        a = k - 1  # 答えの候補
        expected = a | (a + 1)  # a の 1 の桁が全て1の数字で一番小さい数字

        if expected <= n:  # expected が使えるなら、 a の値が & で作れる a & expected
            print(a)
        else:   # expected が使えないなら a & a - 1 が最大値
            print(a - 1)

