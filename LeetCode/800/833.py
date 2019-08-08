class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        converter = {}  # index to convert: converted string

        conditions = {}
        for i, s, t in zip(indexes, sources, targets):
            conditions[i] = (s,t)

        ans = ''
        i = 0
        while i < len(S):
            if i in conditions:
                source, target = conditions[i]
                if S[i:].startswith(source):
                        ans += target
                        i += len(source)
                        continue
            ans += S[i]
            i += 1
        return ans