class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zero_count = 0
        int_que = []
        for i in range(len(arr)):
            if arr[i] == 0:
                int_que.append(arr[i])
                int_que.append(arr[i])
            else:
                int_que.append(arr[i])

            arr[i] = int_que.pop(0)