# https://tenka1-2018-beginner.contest.atcoder.jp/tasks/tenka1_2018_a

import itertools
from collections import Counter
import bisect

def main():
    s = input()
    print(s if len(s) == 2 else s[::-1])

if __name__ == '__main__':
    main()
