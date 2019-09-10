class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'

        ans = ''
        is_minus = False
        if numerator < 0:
            is_minus = not is_minus
            numerator = abs(numerator)
        if denominator < 0:
            is_minus = not is_minus
            denominator = abs(denominator)

        if is_minus:
            ans += '-'

        if numerator % denominator == 0:
            return ans + str(numerator // denominator)

        ans += str(numerator // denominator) + '.'
        fraction_digit = numerator % denominator

        fraction = ''
        logs = []
        while True:
            fraction_digit *= 10
            quotient_digit = fraction_digit // denominator
            fraction_digit = fraction_digit % denominator

            if fraction_digit == 0:
                fraction += str(quotient_digit)
                break

            if (fraction_digit, quotient_digit) in logs:
                index = logs.index((fraction_digit, quotient_digit))
                fraction = fraction[:index] + '(' + fraction[index:] + ')'
                break

            logs.append((fraction_digit, quotient_digit))
            fraction += str(quotient_digit)

        return ans + fraction
