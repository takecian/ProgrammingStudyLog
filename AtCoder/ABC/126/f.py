# https://atcoder.jp/contests/abc126/tasks/abc126_f
import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    M, K = map(int, input().split())

    if M == 0:
        if K == 0:
            print('0 0')
        else:
            print('-1')
        exit()
    if M == 1:
        if K == 0:
            print('0 0 1 1')
        else:
            print('-1')
        exit()

    if 2 ** M <= K:
        print('-1')
    else:
        a = [i for i in range(2 ** M) if i != K]
        b = reversed(a)
        ans = ' '.join(map(str, a)) + ' ' + str(K) + ' ' + ' '.join(map(str, b)) + ' ' + str(K)
        print(ans)

if __name__ == '__main__':
    main()
