import itertools
from collections import Counter
import bisect

def main():
    x, a, b = map(int, input().split())
    print("A" if abs(a - x) < abs(b - x) else "B")

if __name__ == '__main__':
    main()
