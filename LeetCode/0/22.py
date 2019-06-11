

class Solution:
    def generateParenthesis(self, n):
        if not n or n == 0:
            return []
        if n == 1:
            return ["()"]

        l = 2 * n
        res = []
        queue = ["("]
        while queue:
            cur = queue.pop()
            if len(cur) == l - 1:
                cur += ")"
                res.append(cur)
            else:
                op, cl = cur.count("("), cur.count(")")
                if op < n:
                    queue.append(cur + "(")
                if cl < op and cl < n:
                    queue.append(cur + ")")
        return res

s = Solution()
print(s.generateParenthesis(3))
