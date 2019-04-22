# https://atcoder.jp/contests/arc080/tasks/arc080_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for a in A:
        if a % 4 == 0:
            B.append(2)
        elif a % 2 == 0:
            B.append(1)
        else:
            B.append(0)
    four_num = B.count(2)
    two_num = B.count(1)
    one_num = B.count(0)

    if two_num == 0:
        if four_num >= one_num - 1:
            print("Yes")
        else:
            print("No")
    else:
        if four_num >= one_num:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
