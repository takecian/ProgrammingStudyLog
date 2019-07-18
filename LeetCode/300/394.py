# https://leetcode.com/problems/decode-string/

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_stack = []
        str_stack = []
        parsed_string = ''
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':

                num_stack.append(num)
                str_stack.append(parsed_string)
                num = 0
                parsed_string = ''
            elif c == ']':
                num = num_stack.pop()
                decoded_string = parsed_string * num
                num = 0

                prev_string = str_stack.pop()
                parsed_string = prev_string + decoded_string
            else:
                parsed_string += c

        return parsed_string

s = Solution()
print(s.decodeString('3[a]2[bc]'))
