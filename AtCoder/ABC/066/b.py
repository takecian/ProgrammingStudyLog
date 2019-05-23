# https://atcoder.jp/contests/abc066/tasks/abc066_b
import itertools
from collections import Counter
from collections import defaultdict
import bisect

def main():
    s = input()
    for i in range(1, len(s) - 1):
        new_s = s[:len(s) - i]
        if len(new_s) % 2 != 0:
            continue
        front = new_s[:len(new_s) // 2]
        back = new_s[len(new_s) // 2:]
        if front == back:
            print(len(new_s))
            exit()


if __name__ == '__main__':
    main()
