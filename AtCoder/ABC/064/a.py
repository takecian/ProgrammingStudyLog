import itertools
from collections import Counter
from collections import defaultdict
import bisect
import math
import heapq

def main():
    r, g, b = map(int, input().split())
    val = 100 * r + 10 * g + b
    print('YES' if val % 4 == 0 else 'NO')

if __name__ == '__main__':
    main()
