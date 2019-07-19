class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ''
        if len(strs) == 0:
            return ans

        length = min([len(s) for s in strs])
        for i in range(length):
            c = strs[0][i]

            okay = True
            for s in strs:
                if c != s[i]:
                    okay = False
                    break
            if okay:
                ans += c
            else:
                break

        return ans