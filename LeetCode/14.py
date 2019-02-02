# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        answer = ""
        if len(strs) == 0:
            return answer

        min_length = min(map(lambda s: len(s), strs))
        for i in range(min_length):
            c = strs[0][i]
            can_add = True
            for s in strs:
                if s[i] != c:
                    can_add = False
            if can_add:
                answer += c
            else:
                break

        return answer


s = Solution()
print(s.longestCommonPrefix(["aca","cba"]))
# print(s.longestCommonPrefix(["flower","flow","flight"]))
# print(s.longestCommonPrefix( ["dog","racecar","car"]))
