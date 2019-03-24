import itertools
import collections
import bisect

def main():
    X, Y, Z = map(int, input().split())
    X -= Z
    print(X // (Y + Z))

if __name__ == '__main__':
    main()
