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


if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))
