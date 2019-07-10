# https://leetcode.com/problems/strobogrammatic-number/
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        converter = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6', }
        cannot_convert_set = {'2', '3', '5', '4', '7'}

        rotated = []
        for n in num:
            if n in cannot_convert_set:
                return False
            rotated.append(converter[n])
        rotated.reverse()
        rotated_str = ''.join(rotated)
        # print(rotated_str)
        return num == rotated_str