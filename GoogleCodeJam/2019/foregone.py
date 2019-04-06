import itertools
import collections
import bisect

def main():
    N = int(input())
    for i in range(N):
        s = int(input())
        for j in range(1, s):
            if list(str(j)).count('4') > 0:
                continue
            rest = s - j
            if list(str(rest)).count('4') > 0:
                continue
            print("Case #{}: {} {}".format(i + 1, j, rest))
            break

if __name__ == '__main__':
    main()
