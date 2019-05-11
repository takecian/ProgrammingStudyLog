import itertools
import collections
import bisect

def main():
    N = int(input())
    A = [0] + list(map(int, input().split())) + [0]

    total = 0
    for i in range(1, N + 2):
        total += abs(A[i] - A[i-1])

    for i in range(1, N + 1):
        org = abs(A[i] - A[i - 1]) + abs(A[i + 1] - A[i])
        skip = abs(A[i+1] - A[i - 1])
        diff = org - skip
        print(total - diff)


if __name__ == '__main__':
    main()
