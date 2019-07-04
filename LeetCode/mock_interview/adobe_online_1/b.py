class Solution:
    def addStrings(self, num1, num2):
        diff = abs(len(num1) - len(num2))
        if len(num1) > len(num2):
            for i in range(diff):
                num2 = '0' + num2
        else:
            for i in range(diff):
                num1 = '0' + num1

        # print(num1)
        # print(num2)
        input1 = list(map(lambda x: int(x), list(num1)))
        input2 = list(map(lambda x: int(x), list(num2)))

        input1.reverse()
        input2.reverse()

        carry = 0
        ans = ''
        for a, b in zip(input1, input2):
            s = a + b + carry
            ans = str(s % 10) + ans
            if s > 9:
                carry = 1
            else:
                carry = 0
        if carry == 1:
            ans = '1' + ans
        return ans

s = Solution()
print(s.addStrings('12', '12345'))

