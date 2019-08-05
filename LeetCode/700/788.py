class Solution:
    def rotatedDigits(self, N: int) -> int:
        invalids = (3, 4, 7)
        converter = {'1': '1', '0': '0', '8': '8', '2': '5', '5': '2', '6': '9', '9': '6'}
        ans = 0
        for i in range(1, N + 1):
            str_i = str(i)
            is_invalid = False
            for inval in invalids:
                if str(inval) in str_i:
                    is_invalid = True
                    break
            if is_invalid:
                continue
            converted_i = ''.join([converter[c] for c in str_i])
            if str_i != converted_i:
                # print(str_i)
                ans += 1
        return ans
