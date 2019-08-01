class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)
        result = [0] * (len1 + len2)

        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                p1 = i + j
                p2 = i + j + 1
                prod = int(num1[i]) * int(num2[j]) + result[p2]

                result[p1] += prod // 10
                result[p2] = prod % 10
                print(result)

        ans = ''
        leading_zero = True
        for c in result:
            if c != 0:
                leading_zero = False
            if not leading_zero:
                ans += str(c)

        return ans if len(ans) > 0 else '0'


s = Solution()
print(s.multiply('123', '123'))
