# https://atcoder.jp/contests/cpsco2019-s1/tasks/cpsco2019_s1_b
import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    S = list(input())
    c = Counter(S)
    count = c.most_common()[0][1]
    for key, value in c.items():
        if count != value:
            print('No')
            exit()
    print('Yes')


if __name__ == '__main__':
    main()
