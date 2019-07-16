class Solution(object):
    def gcd(self, a, b):
        if b == 0:
            return a
        if a % b == 0:
            return b
        else:
            return self.gcd(b, a % b)

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        ans = ''

        len1 = len(str1)
        len2 = len(str2)
        gcd_len = self.gcd(max(len1, len2), min(len1, len2))

        candidate = ''
        for c1, c2 in zip(list(str1), list(str2)):
            if c1 == c2:
                candidate += c1
            else:
                break
        # print(candidate)

        if len(candidate) == 0:
            return ''

        candidate = candidate[:gcd_len]

        while len(candidate) > 0:
            if str1.count(candidate) == len1 // len(candidate) and str2.count(candidate) == len2 // len(candidate):
                break
            else:
                candidate = candidate[:-1]
            if len(candidate) == 0:
                break

        return candidate