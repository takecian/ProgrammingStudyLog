

count = int(input())
li = list(map(int, input().split()))

sli = sorted(li)

# print(li)
# print(sli)

default_median_index = int((len(sli) + 1) / 2)
default_median = sli[default_median_index]

# print(default_median_index)
# print(default_median)

for i in range(len(li)):
    r = li[i]
    if r < default_median:
        print(default_median)
    else:
        print(sli[default_median_index - 1])

