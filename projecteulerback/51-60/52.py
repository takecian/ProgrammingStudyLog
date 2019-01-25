# https://projecteuler.net/archives;page=2
#
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.


def has_same_digits(a, b):
    al = sorted(list(str(a)))
    bl = sorted(list(str(b)))
    return al == bl


for i in range(1, 10000000):
    if has_same_digits(i, i*2) and has_same_digits(i*3, i*4) and has_same_digits(i*5, i*6):
        if has_same_digits(i, i*3) and has_same_digits(i, i*3):
            print(i)
            break

