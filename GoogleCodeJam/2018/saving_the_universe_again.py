

def damage(p):
    attack = 1
    damage = 0
    for i in p:
        if i == 'C':
            attack = attack * 2
        if i == 'S':
            damage = damage + attack

    return damage


def bubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if a[j] > a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                return a
    return a


def solve(w, p):
    d = damage(p)
    s = 0

    if d <= w:
        return str(s)

    while True:
        p = bubbleSort(p)
        s = s + 1

        new_damage = damage(p)

        if new_damage <= w:
            return str(s)
        if new_damage == d:
            return "IMPOSSIBLE"


number_questions = input("Please enter something: ")
for i in range(int(number_questions)):
   w, p = input("input question: ").split()
   p = list(p)
   a = solve(int(w), p)
   print("Case #{}: {}".format(i + 1, a))


