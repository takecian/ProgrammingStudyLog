# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())
    book = {}
    for _ in range(N):
        name, phone  = input().split()
        book[name] = phone
    for _ in range(N):
        n = input()
        if n in book:
            print("{}={}".format(n, book[n]))
        else:
            print("Not found")


if __name__ == '__main__':
    main()
