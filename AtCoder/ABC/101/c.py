# https://atcoder.jp/contests/abc101/tasks/arc099_a
import math


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # print("{}, {}, {}".format(N-1, K-1, (N-1)/(K-1)))
    print(math.ceil((N-1)/(K-1)))


if __name__ == '__main__':
    main()
