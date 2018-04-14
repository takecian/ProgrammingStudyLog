# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(value):
    val_str = str(value)
    rev_str = val_str[::-1]
    return val_str == rev_str


for i in range(999, 100, -1):
    x = i

    for j in range(i, 1000):
        val = x * j
        if is_palindrome(val):
            print(val)
            exit(0)
        x -= 1

    x = i-1
    for j in range(i, 1000):
        val = x * j
        if is_palindrome(val):
            print(val)
            exit(0)
        x -= 1

