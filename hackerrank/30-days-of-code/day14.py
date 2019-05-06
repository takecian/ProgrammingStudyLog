class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        pass

    def get_maximumDifference(self):
        mi = 100
        ma = 0
        for e in self.__elements:
            mi = min(mi, e)
            ma = max(ma, e)
        return abs(mi - ma)

    maximumDifference = property(get_maximumDifference)

# End of Difference class