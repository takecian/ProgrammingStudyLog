def knapsackProblem(items, capacity):
    # Write your code here.
    item_count = len(items)

    dp = [[0] * (capacity + 1) for _ in range(item_count + 1)]

    for i in range(1, item_count + 1):
        for j in range(capacity + 1):
            value = items[i - 1][0]
            weight = items[i - 1][1]
            if weight <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
            else:
                dp[i][j] = dp[i - 1][j]

    return [dp[-1][-1], build_items(items, dp)]


def build_items(items, dp):
    seq = []
    i = len(dp) - 1
    cost = len(dp[0]) - 1
    while i > 0:
        if dp[i][cost] == dp[i - 1][cost]:  # not used
            i -= 1
        else:
            seq.append(i - 1)
            cost -= items[i - 1][1]
            i -= 1
        if cost == 0:
            break

    seq.reverse()
    return seq