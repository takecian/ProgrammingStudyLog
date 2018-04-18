# https://projecteuler.net/problem=36
#
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)


def is_bin_palindromic(n):
    b = format(n, "b")
    l = list(b)
    rl = l[::-1]
    # print(l)
    # print(rl)
    return l == rl


def is_palindromic(n):
    l = list(str(n))
    rl = l[::-1]
    # print(l)
    # print(rl)
    return l == rl


total = 0
for i in range(1,1000000,2):  # check only odd number
    # print(i)
    if is_palindromic(i) and is_bin_palindromic(i):
        total += i

print(total)