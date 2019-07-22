class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        type_s = ''
        for s in S:
            if s == '#':
                type_s = type_s[:-1]
            else:
                type_s += s
        type_t = ''
        for t in T:
            if t == '#':
                type_t = type_t[:-1]
            else:
                type_t += t
        return type_s == type_t