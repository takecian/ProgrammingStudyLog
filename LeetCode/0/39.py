class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def pattern(candi, rest):
            if rest == 0:
                return [[]]

            next_ptn = []
            for i in range(len(candi)):
                if candi[i] <= rest:
                    for p in pattern(candi[i:], rest - candi[i]):
                        p.append(candi[i])
                        next_ptn.append(p)
            return next_ptn

        return pattern(candidates, target)


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        def try_patterns(ptn, rest):
            if rest == 0:
                ans.append(ptn)
            else:
                for c in candidates:
                    if len(ptn) == 0 or ptn[-1] <= c:
                        if c <= rest:
                            try_patterns(ptn + [c], rest - c)

        try_patterns([], target)

        return ans

