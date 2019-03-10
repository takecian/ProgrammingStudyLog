import itertools
import collections
import bisect

# bin(10*12) = '0b1110100011010100101001010001000000000000' -> 40桁あればよい
def calc(x, b):
    if b == 0:
        return x // 2 + x % 2
    base = 2 ** b
    if x < base:
        return 0

    if (x // base) % 2:
        return base * ((x // base) // 2) + x % base + 1
    else:
        return base * ((x // base) // 2)


def main():
    A, B = map(int, input().split())

    bits = []
    for i in range(41):
        a = calc(max(0, A-1), i)
        b = calc(max(0, B), i)
        bits.append(abs(b - a) % 2)

    for i in range(20):
        print("{} {} {} {}".format(calc(i, 3), calc(i, 2), calc(i, 1), calc(i, 0)))
    exit()

    # print(bits)
    ans = 0
    for i in range(len(bits)):
        ans += bits[i] * (2 ** i)
    print(ans)


if __name__ == '__main__':
    main()
