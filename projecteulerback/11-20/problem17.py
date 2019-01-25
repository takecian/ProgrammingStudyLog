# https://projecteuler.net/problem=17

f = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
s = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

h = "hundred"
a = "and"


def convert(n):
    if n < 20:
        return f[n]
    if n < 100:
        d = list(str(n))
        return s[int(d[0])] + f[int(d[1])]
    if n == 100:
        return "one" + h
    if n < 1000:
        d = list(str(n))
        low = convert(int(d[1]) * 10 + int(d[2]))
        # print(low)
        if len(low) > 0:
            return f[int(d[0])] + h + a + low
        else:
            return f[int(d[0])] + h
    return "onethousand"


# print(convert(1000))
total = 0
for i in range(1, 1001):
    # print(convert(i))
    total += len(convert(i))

print(total)
