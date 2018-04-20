
n = 1
d = 0
ans = 1

for i in range(1, 7):
    c = 9 * 10**(i - 1) * i
    while n < d + c:
        # find value
        print("target = " + str(n))
        index = n - d - 1
        # print("offset = " + str(offset))

        num_index = index // i
        offset = index % i

        number = 10**(i - 1) + num_index
        val = int(list(str(number))[offset])
        print("number = " + str(number) + ", offset = " + str(offset) + ", val = " + str(val))
        ans *= val
        n *= 10
    d += c


print("answer = " + str(ans))
