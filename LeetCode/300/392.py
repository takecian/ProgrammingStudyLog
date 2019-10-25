class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        ti = 0

        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1
                ti += 1
            else:
                ti += 1

        return si == len(s)


from collections import defaultdict
import bisect

    def isSubsequence2(self, s: str, t: str) -> bool:

        charindex = defaultdict(list)
        for i in range(len(t)):
            charindex[t[i]].append(i)

        si = 0
        ti = 0
        while si < len(s):
            ilist = charindex[s[si]]
            if len(ilist) == 0:
                return False

            index = bisect.bisect_left(ilist, ti)
            if index == len(ilist):
                return False

            si += 1
            ti = ilist[index] + 1

        return True
