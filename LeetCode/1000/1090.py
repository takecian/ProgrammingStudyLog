from collections import defaultdict


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        label_values = []
        n = len(values)
        for i in range(n):
            label_values.append((values[i], labels[i]))

        label_values.sort(key=lambda lv: -lv[0])

        labels_used = defaultdict(lambda: 0)
        ans = 0
        count = 0
        for v, l in label_values:
            if labels_used[l] == use_limit:
                continue
            ans += v
            labels_used[l] += 1
            count += 1
            if count == num_wanted:
                break
        return ans
