# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lines = [[] for _ in range(numRows)]
        s_list = list(s)

        while len(s_list) > 0:
            # print(s_list)
            for i in range(numRows):
                if len(s_list) == 0:
                    break
                lines[i].append(s_list.pop(0))
            for i in range(numRows - 2, 0, -1):
                # print(i)
                if len(s_list) == 0:
                    break
                lines[i].append(s_list.pop(0))
            if len(s_list) == 0:
                break

        answer = []
        for l in lines:
            answer += l

        return ''.join(answer)

    def convert2(self, s: str, numRows: int) -> str:
        strings = [[] for _ in range(numRows)]

        index = 0
        isDown = True
        for c in s:
            strings[index].append(c)

            if numRows > 1:
                if isDown:
                    if index == numRows - 1:
                        index -= 1
                        isDown = False
                    else:
                        index += 1
                else:
                    if index == 0:
                        index += 1
                        isDown = True
                    else:
                        index -= 1

        ans = ''
        for sl in strings:
            ans += ''.join(sl)

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))
