# https://abs.contest.atcoder.jp/tasks/abc086_a

def check(a, b):
    isEven = (a * b) % 2 == 0
    if isEven:
        print("Even")
    else:
        print("Odd")


a, b = input("").split()
check(int(a), int(b))
