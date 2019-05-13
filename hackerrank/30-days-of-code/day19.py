

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        if n == 1:
            return 1
        i = 1
        ans = 0
        while i * i <= n:
            if n % i == 0:
                if i == n // i:
                    ans += i
                else:
                    ans += i + n // i
            i += 1
        return ans



n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)