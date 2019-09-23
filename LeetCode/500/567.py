class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_l = [0] * 26
        for c1 in s1:
            s1_l[ord(c1) - ord('a')] += 1

        s2_l = [0] * 26
        for c2 in s2[:len(s1)]:
            s2_l[ord(c2) - ord('a')] += 1
        if s1_l == s2_l:
            return True
        for i in range(len(s1), len(s2)):
            s2_l[ord(s2[i - len(s1)]) - ord('a')] -= 1
            s2_l[ord(s2[i]) - ord('a')] += 1
            if s1_l == s2_l:
                return True
        return False