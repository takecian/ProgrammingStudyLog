# https://atcoder.jp/contests/abc121/tasks/abc121_d

import itertools
import collections
import bisect

# bin(10*12) = '0b1110100011010100101001010001000000000000' -> 40桁あればよい
# def calc(x, b):
#     if b == 0:
#         return x // 2 + x % 2
#     base = 2 ** b
#     if x < base:
#         return 0
#
#     if (x // base) % 2:
#         if x // base == 1:
#             return x % base + 1
#         else:
#             return x // 2 + x % base + 1
#     else:
#         return x // 2
#
#
# def main():
#     A, B = map(int, input().split())
#
#     bits = []
#     for i in range(41):
#         a = calc(max(0, A-1), i)
#         b = calc(max(0, B), i)
#         bits.append(abs(b - a) % 2)
#
#     print(bits)
#     ans = 0
#     for i in range(len(bits)):
#         ans += bits[i] * (2 ** i)
#     print(ans)

def calc(x):
    if x % 2:  # 奇数なら 1 or 0
        if x % 4 == 1:
            return 1
        else:
            return 0
    else:
        if x % 4 == 0:
            return x
        else:
            return x ^ 1

def main():
    A, B = map(int, input().split())
    ans = calc(B) ^ calc(max(0, A-1))
    print(ans)

if __name__ == '__main__':
    main()
