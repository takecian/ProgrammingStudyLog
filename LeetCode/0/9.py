# https://leetcode.com/problems/palindrome-number/


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    return str(x) == str(x)[::-1]

isPalindrome(121)
