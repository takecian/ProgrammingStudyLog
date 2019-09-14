class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        left = 0
        right = stations[-1] - stations[0]
        while left + 10**(-6) < right:
            mid = (left + right) / 2
            count = 0
            for i in range(len(stations)-1):
                count += math.ceil((stations[i+1]-stations[i]) / mid) - 1
            if count > K:
                left = mid
            else:
                right = mid
        return left