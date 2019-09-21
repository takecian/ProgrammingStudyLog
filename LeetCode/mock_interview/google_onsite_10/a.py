class Solution:
    def removeDuplicates(self, S: str) -> str:
        que = []
        for c in S:
            if len(que) == 0:
                que.append(c)
                continue

            if que[-1] == c:
                que.pop()
            else:
                que.append(c)
        return ''.join(que)
