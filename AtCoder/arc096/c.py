import sys

a, b, c, x, y = map(int, input().split())

best_price = sys.maxsize


for i in range(0, max(x, y) * 2 + 1, 2):
    rest_a = x
    rest_b = y

    if i // 2 >= x:
        rest_a = 0
    else:
        rest_a = x - i // 2

    if i // 2 >= y:
        rest_b = 0
    else:
        rest_b = y - i // 2

    price = rest_a * a + rest_b * b + c * i
    if price < best_price:
        best_price = price
    # print("buy a = " + str(rest_a) + ", b = " + str(rest_b) + ", c = " + str(i) + ", price = " + str(price))

print(best_price)

