import heapq


def findThreeLargestNumbers(array):
    # Write your code here.
    que = []
    for num in array:
        heapq.heappush(que, -num)

    ans = []
    for _ in range(3):
        ans.append(-heapq.heappop(que))
    ans.reverse()
    return ans
