class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        result = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                pos1 = i + j
                pos2 = i + j + 1
                val = int(num1[i]) * int(num2[j]) + result[pos2]
                result[pos1] += val // 10
                result[pos2] = val % 10

        offset = 0
        while offset < (n1 + n2) - 1 and result[offset] == 0:
            offset += 1
        return ''.join(map(str, result[offset:]))