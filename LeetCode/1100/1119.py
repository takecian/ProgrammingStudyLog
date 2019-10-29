class Solution:
    def removeVowels(self, S: str) -> str:
        return S.replace('a', '').replace('i', '').replace('u', '').replace('e', '').replace('o', '')
