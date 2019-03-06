# https://atcoder.jp/contests/abc106/tasks/abc106_c

import itertools
import collections
import bisect

def main():
    S = input()
    K = int(input())

    # 途中に１以外の数字があればそれが答え
    for i in range(len(S)):
        if S[i] != '1':
            print(S[i])
            exit()
        elif i == K - 1:
            print(S[i])
            exit()


if __name__ == '__main__':
    main()
