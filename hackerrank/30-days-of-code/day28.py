#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

    gmail_names = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if re.match('.*@gmail.com', emailID):
            gmail_names.append(firstName)

    gmail_names.sort()
    for n in gmail_names:
        print(n)
