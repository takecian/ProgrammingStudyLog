import heapq

def heapSort(array):
    # Write your code here.
    que = []
    for num in array:
        heapq.heappush(que, num)

    ans = []
    while len(que):
        val = heapq.heappop(que)
        ans.append(val)
    return ans
