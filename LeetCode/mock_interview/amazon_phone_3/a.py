class Solution:
    def firstUniqChar(self, s: str) -> int:
        once = set()
        morethan = set()
        for i, v in enumerate(s):
            if v in morethan:
                continue
            if v in once:
                once.remove(v)
                morethan.add(v)
                continue
            if v not in once:
                once.add(v)

        for i, v in enumerate(s):
            if v in once:
                return i
        return -1