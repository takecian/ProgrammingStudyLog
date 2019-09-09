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