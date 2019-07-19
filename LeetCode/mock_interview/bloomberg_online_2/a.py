class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(numRows):
            ans.append([1] * (i + 1))

        for i in range(2, numRows):
            length = i + 1
            # from 2rows
            for j in range(1, length - 1):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]

        return ans
