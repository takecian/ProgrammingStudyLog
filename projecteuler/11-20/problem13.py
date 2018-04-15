# https://projecteuler.net/problem=13

data = open("input13.txt", "r")

lines = list(map(int, data.readlines()))

data.close()

print(sum(lines))

# 5537376230390876637302048746832985971773659831892672