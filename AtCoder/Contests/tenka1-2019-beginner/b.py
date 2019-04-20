# https://tenka1-2019-beginner.contest.atcoder.jp/tasks/tenka1_2019_b

import itertools
from collections import Counter
import bisect

def main():
    N = int(input())
    S = input()
    K = int(input())
    K -= 1
    target = S[K]
    ans = ''
    for s in S:
        ans += '*' if s != target else s
    print(ans)


if __name__ == '__main__':
    main()
