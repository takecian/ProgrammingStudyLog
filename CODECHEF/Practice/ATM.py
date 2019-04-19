import itertools
import collections
import bisect

def main():
    X, Y = map(float, input().split())
    if X % 5 == 0 and X + 0.5 <= Y:
        print(Y - X - 0.5)
    else:
        print(Y)

if __name__ == '__main__':
    main()
