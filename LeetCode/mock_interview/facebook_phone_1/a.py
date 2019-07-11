import bisect
from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        # dones = defaultdict(set)
        nums.sort()
        for i in range(len(nums) - 2):
            a = nums[i]
            target = - a
            l = i + 1
            r = len(nums) - 1
            while l < r:
                b = nums[l]
                c = nums[r]
                if b + c == target:
                    # candidates = [a,b,c]
                    # candidates.sort()
                    # if candidates[0] not in dones:
                    #     dones[candidates[0]].add({candidates[1]: { candidates[2] }})
                    #     ans.append(candidates)
                    # else:
                    #     if candidates[1] not dones[candidates[0]]:

                    ans.add((a, b, c))
                    l += 1
                    r -= 1
                else:
                    if b + c < target:
                        l += 1
                    else:
                        r -= 1
        return [[a, b, c] for a, b, c in ans]