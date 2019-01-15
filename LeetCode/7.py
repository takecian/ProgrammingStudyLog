class Solution:
    def reverse(self, x):
        is_positive = x > 0
        abs_x = abs(x)
        reverse_abs_x = int("".join(reversed(str(abs_x))))

        reverse_abs_x = 0 if (2 ** 31 - 1) <= reverse_abs_x else reverse_abs_x
        return reverse_abs_x if is_positive else -reverse_abs_x
