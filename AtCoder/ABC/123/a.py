

import itertools
import collections
import bisect

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if e - a <= k:
        print('Yay!')
    else:
        print(':(')

if __name__ == '__main__':
    main()
