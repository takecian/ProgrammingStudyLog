class Solution:
    def reverse(self, x: int) -> int:
        str_x = list(str(x))
        str_x.reverse()
        if x < 0:
            str_x = str_x[:-1]
            str_x = ['-'] + str_x

        ans = int(''.join(str_x))

        max_int = 2 ** 31
        if -max_int <= ans < max_int:
            return ans
        else:
            return 0