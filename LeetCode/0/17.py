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

        answers = []

        for d in digits:
            new_answers = []
            if len(answers) > 0:
                for a in answers:
                    for c in table[d]:
                        new_answers.append(a + c)
                answers = new_answers
            else:
                answers = table[d]
        # print(table)

        return answers


s = Solution()
print(s.letterCombinations("23"))
