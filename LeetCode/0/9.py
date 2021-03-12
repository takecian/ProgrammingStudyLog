# https://leetcode.com/problems/palindrome-number/


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    return str(x) == str(x)[::-1]

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x != 0:
            return False

        reversed_num = 0
        temp = x
        while x > reversed_num:
            reversed_num = reversed_num * 10 + temp % 10
            temp = temp // 10

        print(x)
        print(reversed_num)
        return x == reversed_num

s = Solution()
print(s.isPalindrome(121))

isPalindrome(121)
