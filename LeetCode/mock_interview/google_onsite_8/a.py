class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        tl = text.split(' ')
        for i in range(2, len(tl)):
            if tl[i - 2] == first and tl[i - 1] == second:
                ans.append(tl[i])
        return ans