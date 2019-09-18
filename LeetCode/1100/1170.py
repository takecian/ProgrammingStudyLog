class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def smallest_freq(s):
            slist = list(s)
            slist.sort()
            return slist.count(slist[0])

        queries_v = list(map(lambda w: smallest_freq(w), queries))
        words_v = list(map(lambda w: smallest_freq(w), words))
        ans = []
        for q in queries_v:
            count = 0
            for w in words_v:
                if q < w:
                    count += 1
            ans.append(count)

        return ans