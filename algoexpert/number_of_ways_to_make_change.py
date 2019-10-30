def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    if n == 0:
        return 1
    ans = 0

    def calc(rest, index):
        nonlocal ans
        if rest == 0:
            ans += 1
            return
        if index == len(denoms):
            return

        i = 0
        while denoms[index] * i <= rest:
            calc(rest - denoms[index] * i, index + 1)
            i += 1

    calc(n, 0)
    return ans
