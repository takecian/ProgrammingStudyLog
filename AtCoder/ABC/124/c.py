# https://atcoder.jp/contests/abc124/tasks/abc124_c

import itertools
from collections import Counter
import bisect

def main():
    S = list(input())

    even_black = 0
    even_white = 0
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == '0':  # black
                even_white += 1
            else:  # white
                even_black += 1
        else: # odd
            if S[i] == '0':  # black
                even_black += 1
            else:  # white
                even_white += 1

    print(min(even_black, even_white))


if __name__ == '__main__':
    main()
