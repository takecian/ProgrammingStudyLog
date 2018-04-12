

h, w = map(int, input().split())

results = []

for i in range(int(h)):
    li = list(map(int, input().split()))
    li = list(map(lambda x: "1" if x > 127 else "0", li))
    results.append(li)

for result in results:
    print(" ".join(result))
