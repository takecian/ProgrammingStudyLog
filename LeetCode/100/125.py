import itertools
from collections import Counter
from collections import defaultdict
import bisect
from heapq import heappush, heappop


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = list(filter(lambda c: c.isalnum(), s))
        alpha_string = ''.join(l).lower()
        rev_alpha_string = alpha_string[::-1]
        # print(alpha_string)
        # print(rev_alpha_string)
        return alpha_string == rev_alpha_string

def main():
    s = Solution()
    print(s.isPalindrome('A man, a plan, a canal: Panama'))
    print(s.isPalindrome('OP'))


if __name__ == '__main__':
    main()
