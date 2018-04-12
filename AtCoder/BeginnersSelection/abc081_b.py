
count = int(input())
li = list(map(int, input().split()))

divide = 0

while True:
    res = list(filter(lambda x: x % 2 == 1, li))
    if len(res) > 0:
        print(divide)
        exit(0)
    li = list(map(lambda x: int(x/2), li))
    divide += 1
