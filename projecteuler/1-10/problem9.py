# https://projecteuler.net/problem=9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Solve following equation
# a2 + b2 = c2
# a + b + c = 1000 -> c = 1000 - a - b
# condition: a < 999, b < 999, c < 999
# find a and b which meets `2000*(a+b) - 2 * a * b == 1000**2`


for a in range(1, 999):
    for b in range(1, 999):
        if 2000*(a+b) - 2 * a * b == 1000**2:
            c = 1000 - a - b
            print("a = " + str(a) + ", b = " + str(b) + ", c = " + str(c))
            abc = a * b * c
            print("answer = " + str(abc))
            exit(0)
