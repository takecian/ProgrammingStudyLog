class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for log in logs:
            sp_log = log.split(' ')
            if sp_log[1].isdigit():
                digits.append(log)
            else:
                letters.append((log, ' '.join(sp_log[1:]), sp_log[0]))
        # print(digits)
        # print(letters)
        letters.sort(key=lambda x: (x[1], x[2]))
        return list(map(lambda x: x[0], letters)) + digits