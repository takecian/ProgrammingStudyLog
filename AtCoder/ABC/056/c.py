
import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop

def main():
    x = int(input())

    i = 1
    while True:
        if i * (i + 1) // 2 >= x:
            print(i)
            break
        i += 1

if __name__ == '__main__':
    main()
    