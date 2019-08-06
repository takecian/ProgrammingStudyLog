class Solution:
    def lengthLongestPath(self, input: str) -> int:

        def dfs(path):
            ans = 0
            current_length = 0

            que = []
            while len(path) > 0:
                prefix = '\t' * len(que)
                if path.startswith(prefix):
                    cur_path = ''
                    index = path.find('\n')
                    if index != -1:  # found
                        cur_path = path[len(prefix):index]
                        path = path[(index + 1):]
                    else:
                        cur_path = path[len(prefix):]
                        path = ''

                    # print(cur_path)
                    if cur_path.count('.') > 0:
                        ans = max(ans, current_length + len(cur_path))
                    else:
                        que.append(cur_path + '/')
                        current_length += len(cur_path + '/')
                        # print(current_length)
                else:
                    pop_dir = que.pop()
                    current_length -= len(pop_dir)

            return ans

        return dfs(input)