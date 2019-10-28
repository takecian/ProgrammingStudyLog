from collections import Counter


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)

        ans = [[]]
        for v, c in counter.items():
            next_ans = []
            for a in ans:
                for i in range((c + 1)):
                    if i == 0:
                        next_ans.append(a)
                    else:
                        next_ans.append(a + [v] * i)
            ans = next_ans
            # print(ans)

        return ans
