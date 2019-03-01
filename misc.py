
# 拡張ユークリッドの互除法：ax + by = gcd(a, b) となる x, y を返す
def extgcd(a, b):
    # ２つの等式を繰り返し引いていく
    x0, y0 = 1, 0  # a = X * x0 + Y * 0 ← 常にこっちの方が大きい
    x1, y1 = 0, 1  # b = X * 0  + Y * y0

    while b:
        q = a // b
        r = a % b
        x2 = x0 - q * x1
        y2 = y0 - q * y1

        a = b
        b = r
        x0, y0 = x1, y1
        x1, y1 = x2, y2

    return a, x0, y0


print(extgcd(12, 21))
