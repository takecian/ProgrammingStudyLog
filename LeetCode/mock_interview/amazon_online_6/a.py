from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter = Counter(chars)
        ans = 0

        for word in words:
            word_counter = Counter(word)
            can_create = True
            for w, c in word_counter.items():
                if w not in chars_counter:
                    can_create = False
                    break
                if c > chars_counter[w]:
                    can_create = False
                    break
            if can_create:
                ans += len(word)
        return ans