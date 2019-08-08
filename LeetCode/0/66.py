class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = int(''.join(list(map(str,digits)))) + 1
        return list(map(int,list(str(val))))
