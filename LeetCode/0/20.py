# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s):
        stack = []
        push_e = [ "(", "{", "["]
        mapping = { "(": ")", "{": "}", "[" : "]"}
        valid = True
        for b in s:
            if b in push_e:
                stack.append(b)
            else:
                if len(stack) > 0:
                    p = stack.pop()
                    if mapping[p] != b:
                        valid = False
                        break
                else:
                    valid = False
                    break

        return len(stack) == 0 and valid

s = Solution()
print(s.isValid(""))
