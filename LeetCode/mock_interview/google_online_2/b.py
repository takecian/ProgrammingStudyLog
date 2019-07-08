
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        ans = 0
        next_pair = None
        kinds = set()
        begin = None

        for i in range(len(tree)):
            if not next_pair:
                next_pair = (tree[i], i)
                kinds.add(next_pair[0])
                begin = 0
                ans = 1
                continue

            if len(kinds) < 2 or tree[i] in kinds:
                kinds.add(tree[i])
                if next_pair[0] != tree[i]:
                    next_pair = (tree[i], i)
            else:
                kinds.clear()
                begin = next_pair[1]
                kinds.add(next_pair[0])
                next_pair = (tree[i], i)
                kinds.add(next_pair[0])

            ans = max(ans, i - begin + 1)
        return ans
