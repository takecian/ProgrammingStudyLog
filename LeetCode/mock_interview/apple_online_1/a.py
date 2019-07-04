class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        victim = len(nums) - 1
        current = 0
        while current < victim:
            if nums[current] == val:
                while 0 < victim and nums[victim] == val:
                    victim -= 1
                if victim == 0:
                    break
                if victim < current:
                    break
                temp = nums[victim]
                nums[victim] = nums[current]
                nums[current] = temp

            current += 1

        return len(nums) - nums.count(val)
