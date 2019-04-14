import itertools
from collections import Counter
import bisect

def main():
    N, K = map(int, input().split())
    S = list(input())

    TYOKU = '0'
    SAKA = '1'

    if S.count(TYOKU) <= K:
        print(N)
        exit()

    asyu = []
    prev = S[0]
    prev_c = 0
    for s in S:
        if prev == s:
            prev_c += 1
        else:
            asyu.append((prev, prev_c))
            prev = s
            prev_c = 1
    asyu.append((prev, prev_c))
    # print(asyu)

    de = []
    for i in range(len(asyu)):
        pair = asyu[i]
        if pair[0] == '0':
            if i > 0:
                prev_pair = asyu[i-1]
                de.append(pair[1] + prev_pair[1])
            else:
                de.append(pair[1])
    # print(de)

    ans = 0
    val = 0
    k = 0
    del_i = 0
    for i in range(len(asyu)):
        pair = asyu[i]
        if pair[0] == '0':
            if k < K:
                val += pair[1]
                k += 1
            else: # max
                val += pair[1]
                val -= de[del_i]
                del_i += 1
        else:
            val += pair[1]
        ans = max(ans, val)

    print(ans)


if __name__ == '__main__':
    main()
