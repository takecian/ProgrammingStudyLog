import bisect

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    ans = []
    diff = 10 ** 15

    arrayTwo.sort()

    for one in arrayOne:
        pos = bisect.bisect_right(arrayTwo, one)
        if abs(one - arrayTwo[pos - 1]) < diff:
            diff = abs(one - arrayTwo[pos - 1])
            ans = [one, arrayTwo[pos - 1]]
        if pos != len(arrayTwo):
            if abs(one - arrayTwo[pos]) < diff:
                diff = abs(one - arrayTwo[pos])
                ans = [one, arrayTwo[pos]]

    return ans
