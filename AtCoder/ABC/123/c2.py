import itertools
import collections
import bisect
import math

def main():
    N = int(input())
    last = N
    for i in range(5):
        s = int(input())
        last = min(last, s)

    ans = math.ceil(N / last) + 4
    print(ans)

if __name__ == '__main__':
    main()
