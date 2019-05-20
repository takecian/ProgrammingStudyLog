#
import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    s = input()
    front = int(s[0:2])
    back = int(s[2:4])
    if 0 < front < 13:  # front can be month
        if 0 < back < 13: # back can be month
            print('AMBIGUOUS')
        else: # back can not be month
            print('MMYY')
    else: # front can not be month
        if 0 < back < 13: # back can be month
            print('YYMM')
        else: # back can not be month
            print('NA')


if __name__ == '__main__':
    main()
