
def gcd(a, b):
    a = max(a, b)
    b = min(a, b)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    a = max(a, b)
    b = min(a, b)
    return a * b * gcd(a, b)
