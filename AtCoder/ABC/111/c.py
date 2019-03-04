# https://atcoder.jp/contests/abc111/tasks/arc103_a

n = int(input())
v = list(map(int, input().split()))

f_l = v[::2]
s_l = v[1::2]


def count_and_sort(l):
    dict = {}
    for f in l:
        if f not in dict:
            dict[f] = 1
        else:
            dict[f] += 1
    return sorted(dict.items(), key=lambda x: -x[1])


f_sorted = count_and_sort(f_l)
s_sorted = count_and_sort(s_l)

f1 = f_sorted[0]
s1 = s_sorted[0]

f2 = f_sorted[1] if len(f_sorted) > 1 else (0, 0)
s2 = s_sorted[1] if len(s_sorted) > 1 else (0, 0)

if f1[0] == s1[0]:  # 同じ値だったら使えないので、どっちかを次の要素で置換する必要がある
    print(min(n - f1[1] - s2[1], (n - f2[1] - s1[1])))
else:
    print(n - f1[1] - s1[1])
