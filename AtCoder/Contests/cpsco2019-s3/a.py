# https://atcoder.jp/contests/cpsco2019-s3/tasks/cpsco2019_s3_a

import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    S = list(input())
    ans = []
    for s in S:
        if s == 'O':
            ans.append('A')
        elif s == 'A':
            ans.append('O')
        else:
            ans.append(s)
    print(''.join(ans))


if __name__ == '__main__':
    main()
