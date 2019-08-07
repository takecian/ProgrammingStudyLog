class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        counters = [[0] * 26 for _ in range(len(A))]
        for i in range(len(A)):
            for c in A[i]:
                counters[i][ord(c) - ord('a')] += 1
        ans = []
        for index, chars in enumerate(zip(*counters)):
            count = min(chars)
            for _ in range(count):
                ans.append(chr(index + ord('a')))
        return ans
