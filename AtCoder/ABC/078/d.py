import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N, Z, W = map(int, input().split())
    a = list(map(int, input().split()))
    if N == 1:
        print(abs(a[0] - W))
    else:
        print(max(abs(a[-1] - W), abs(a[-1] - a[-2])))


if __name__ == '__main__':
    main()