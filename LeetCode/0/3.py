class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_answer = 0
        non_repeat = []
        for c in s:
            if c in non_repeat:
                if len(non_repeat) > 0:
                    non_repeat = non_repeat[non_repeat.index(c) + 1:]
                    non_repeat.append(c)
                else:
                    non_repeat = [c]

            else:
                non_repeat.append(c)
                max_answer = max(max_answer, len(non_repeat))
            # print(dic)
        return max_answer


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("aab"))
