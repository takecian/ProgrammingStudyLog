# https://atcoder.jp/contests/abc101/tasks/arc099_a
import math


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # print("{}, {}, {}".format(N-1, K-1, (N-1)/(K-1)))
    # 一度の操作でたかだか K-1 個しか 1 を増やせない
    # 1 以外の整数の数は N-1 個
    print(math.ceil((N-1)/(K-1)))


if __name__ == '__main__':
    main()
