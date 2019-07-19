class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        org = [c for c in cells]
        ptns_c = 0
        ptns = { str(cells): ptns_c}
        # find loop

        while True:
            cells = [0] + [1 if cells[i - 1] == cells[i + 1] else 0 for i in range(1, 7)] + [0]
            ptns_c += 1

            if str(cells) in ptns:
                break
            else:
                ptns[str(cells)] = ptns_c

        loop = ptns_c - ptns[str(cells)]
        N = (N - ptns[str(cells)]) % loop + ptns[str(cells)]
        cells = org
        # print(N)
        for _ in range(N):
            cells = [0] + [1 if cells[i - 1] == cells[i + 1] else 0 for i in range(1, 7)] + [0]

        return cells