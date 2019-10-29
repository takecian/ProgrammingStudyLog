class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        a = a[::-1]
        b = b[::-1]
        carry = 0
        i = 0
        while i < min(len(a), len(b)):
            val = carry
            val += 1 if a[i] == '1' else 0
            val += 1 if b[i] == '1' else 0
            carry = 1 if val // 2 == 1 else 0
            val = val % 2
            ans += str(val)
            i += 1

        for j in range(i, len(a)):
            val = carry
            val += 1 if a[j] == '1' else 0
            carry = 1 if val // 2 == 1 else 0
            val = val % 2
            ans += str(val)

        for j in range(i, len(b)):
            val = carry
            val += 1 if b[j] == '1' else 0
            carry = 1 if val // 2 == 1 else 0
            val = val % 2
            ans += str(val)

        if carry:
            ans += '1'
        ans = ans[::-1]
        return ans
