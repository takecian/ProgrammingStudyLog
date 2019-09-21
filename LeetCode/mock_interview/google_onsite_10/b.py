class Solution:
    def expand(self, S: str) -> List[str]:
        ans = ['']
        i = 0
        while i < len(S):
            next_ans = []
            if S[i] != '{':
                for word in ans:
                    next_ans.append(word + S[i])
                i += 1
            else:
                close_index = S[i:].index('}')
                options = S[i + 1:i + close_index].split(',')
                # print(options)
                for word in ans:
                    for option in options:
                        next_ans.append(word + option)
                i += close_index + 1

            ans = next_ans
            # print(ans)
        ans.sort()
        return ans