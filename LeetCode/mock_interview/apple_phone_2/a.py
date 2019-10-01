class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        n = len(persons)
        counter = [0] * n
        self.leadings = []
        leader = 0
        for p, t in zip(persons, times):
            counter[p] += 1
            if counter[p] >= counter[leader]:
                leader = p

            self.leadings.append((t, leader))

    def q(self, t: int) -> int:
        l = 0
        r = len(self.leadings)

        while l < r:
            m = (l + r) // 2
            mt = self.leadings[m][0]
            if mt <= t:
                l = m + 1
            else:
                r = m
        # print(l, r)
        return self.leadings[r - 1][1]
