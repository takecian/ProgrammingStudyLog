# https://projecteuler.net/problem=48

total = 0
for i in range(1,1001):
    total += i ** i

print(str(total)[-10::])