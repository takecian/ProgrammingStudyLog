
import itertools
import collections
import bisect

def main():
    N = int(input())
    A = list(map(int, input().split()))
    c = collections.Counter(A)
    ans = sum([count // 2 for count in c.values()])
    print(ans)


if __name__ == '__main__':
    main()
