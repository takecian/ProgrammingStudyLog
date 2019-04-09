import itertools
import collections
import bisect

def main():
    N = int(input())
    for i in range(N):
        s = list(input())
        ans1 = ''
        ans2 = ''
        for c in s:
            if c == '4':
                ans1 += '3'
                ans2 += '1'
            else:
                ans1 += c
                ans2 += '0'

        print("Case #{}: {} {}".format(i + 1, int(ans1), int(ans2)))


if __name__ == '__main__':
    main()
