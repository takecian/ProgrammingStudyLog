# https://atcoder.jp/contests/abc122/tasks/abc122_b

import itertools
import collections
import bisect

def main():
    S = list(input())
    ans = 0
    current = 0
    for i in range(len(S)):
        if S[i] in ['A', 'C', 'G', 'T']:
            current += 1
            ans = max(ans, current)
        else:
            current = 0
    print(ans)

if __name__ == '__main__':
    main()
