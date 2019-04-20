# https://tenka1-2019-beginner.contest.atcoder.jp/tasks/tenka1_2019_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    A, B, C = map(int, input().split())
    if A < C < B or B < C <A:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
