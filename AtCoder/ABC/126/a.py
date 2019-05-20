# https://atcoder.jp/contests/abc126/tasks/abc126_a
import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N, K = map(int, input().split())
    S = list(input())
    S[K-1] = S[K-1].lower()
    print(''.join(S))

if __name__ == '__main__':
    main()
