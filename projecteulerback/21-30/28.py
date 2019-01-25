# https://projecteuler.net/problem=28
#
#
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


# 1, 9, 25.. = (2n + 1) ** 2

total = 1

for i in range(1, 501):
    total += 4 * (2 * i + 1) ** 2 - 12 * i


print(total)





