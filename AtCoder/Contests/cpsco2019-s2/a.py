import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math

def main():
    M, N = map(int, input().split())
    div = M // N
    print(M - div * (N - 1))

if __name__ == '__main__':
    main()
