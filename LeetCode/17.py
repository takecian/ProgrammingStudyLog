# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        table = {}
        table["2"] = ["a", "b", "c"]
        table["3"] = ["d", "e", "f"]
        table["4"] = ["g", "h", "i"]
        table["5"] = ["j", "k", "l"]
        table["6"] = ["m", "n", "o"]
        table["7"] = ["p", "q", "r", "s"]
        table["8"] = ["t", "u", "v"]
        table["9"] = ["w", "x", "y", "z"]

        answer = []

        print(table)

        return answer


s = Solution()
print(s.letterCombinations("23"))
