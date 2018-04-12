# https://abs.contest.atcoder.jp/tasks/abc081_a
#
# すぬけ君は 1,2,3 の番号がついた 3 つのマスからなるマス目を持っています。 各マスには 0 か 1 が書かれており、マス i には si が書かれています。
#
# すぬけ君は 1 が書かれたマスにビー玉を置きます。 ビー玉が置かれるマスがいくつあるか求めてください。


s = list(input())

count = 0
for i in s:
    if i == "1":
        count += 1

print(count)
