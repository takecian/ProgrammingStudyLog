# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

# Notice that you can not jump outside of the array at any time.

 

# Example 1:

# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation: 
# All possible ways to reach at index 3 with value 0 are: 
# index 5 -> index 4 -> index 1 -> index 3 
# index 5 -> index 6 -> index 4 -> index 1 -> index 3 

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        length = len(arr)
        reachable = [False for _ in range(length)]
        
        que = [start]
        reachable[start] = True
        while que:
            point = que.pop()
            reachable[point] = True

            forward = point + arr[point]
            if forward < length and reachable[forward] == False:
                que.append(forward)
            backward = point - arr[point]
            if 0 <= backward and reachable[backward] == False:
                que.append(backward)

        result = False        
        for i in range(length):
            if arr[i] == 0:
                result = result or reachable[i]
        return result