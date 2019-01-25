# https://projecteuler.net/problem=38

m = 0
for n in range(1, 10000):
    ans = ""
    for i in range(1, 10):
        ans += str(n * i)
        # print(ans)
        if len(ans) > 8:
            break

    is_pandigital = len(ans) == 9 and len(set(ans)) == 9 and "0" not in ans
    if is_pandigital:
        # print(ans)
        if int(ans) > m:
            print("number = " + str(n) + ", 9digit = " + str(ans))
            m = int(ans)

print(m)
