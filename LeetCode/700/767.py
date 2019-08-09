class Solution:
    def reorganizeString(self, S: str) -> str:
        counter = [[0, i] for i in range(26)]
        for c in S:
            counter[ord(c) - ord('a')][0] += 1

        # print(counter)
        counter.sort(key=lambda c: -c[0])

        if counter[0][0] > (len(S) + 1) // 2:
            return ''

        sorted_s = ''.join([chr(c[1] + ord('a')) * c[0] for c in counter])
        # print(sorted_s)
        even = list(sorted_s[:(len(sorted_s) + 1) // 2])
        odd = list(sorted_s[(len(sorted_s) + 1) // 2:])

        ans = ''
        for i in range(len(sorted_s)):
            if i % 2 == 0:
                ans += even.pop(0)
            else:
                ans += odd.pop(0)
        return ans