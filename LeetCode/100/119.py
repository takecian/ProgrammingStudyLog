class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1]]
        for _ in range(rowIndex):
            prev = pascal[-1]
            left = [0] + prev
            right = prev + [0]
            new_line = []
            for l, r in zip(left, right):
                new_line.append(l + r)
            pascal.append(new_line)
        return pascal[-1]