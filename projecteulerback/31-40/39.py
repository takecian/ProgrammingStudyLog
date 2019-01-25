# https://projecteuler.net/problem=39
#
# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

# a = 20
# b = 48
# c = 52
#
# is_triangle = a ** 2 + b ** 2 == c ** 2
#
# print(is_triangle)


m_i = 0
m_s = 0
for i in range(4,1000):
    s = 0
    for a in range(1, int(i/2)):
        for b in range(a, int(i / 2)):
            c = i - a - b
            if a + b < c:
                continue
            if a ** 2 + b ** 2 == c ** 2:
                s += 1

    print(str(i) + ": " + str(s))
    if s > m_s:
        m_s = s
        m_i = i


print(str(m_i) + ": " + str(m_s))