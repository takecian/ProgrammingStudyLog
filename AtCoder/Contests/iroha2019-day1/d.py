import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    taka = X + sum([A[i] for i in range(len(A)) if i % 2 == 0])
    aoki = Y + sum([A[i] for i in range(len(A)) if i % 2 == 1])
    if taka > aoki:
        print("Takahashi")
    elif taka < aoki:
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    main()
