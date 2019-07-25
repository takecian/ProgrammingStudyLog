class Solution(object):
    def confusingNumber(self, N):
        """
        :type N: int
        :rtype: bool
        """
        invalids = [2, 3, 4, 5, 7]
        converter = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

        nlist = list(map(int, list(str(N))))
        for n in nlist:
            if n in invalids:
                return False

        rev_nlist = list(map(lambda n: converter[n], reversed(nlist)))
        # print(nlist)
        # print(rev_nlist)
        return nlist != rev_nlist