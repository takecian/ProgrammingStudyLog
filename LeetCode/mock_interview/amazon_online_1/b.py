class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ans = []
        if len(S) == 0:
            return []
        index = 0
        while index < len(S):
            dones = set()
            target = S[index]
            dones.add(target)
            target_last = S.rfind(target)
            while index < target_last:
                dones.add(S[index])
                target_last = max(target_last, S.rfind(S[index]))
                index += 1
            while index < len(S):
                if S[index] in dones:
                    index += 1
                else:
                    break

            ans.append(index)
        # print(ans)
        for i in range(len(ans) - 1, 0, -1):
            ans[i] = ans[i] - ans[i - 1]

        return ans
