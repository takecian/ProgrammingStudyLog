class Solution:
    def nextClosestTime(self, time: str) -> str:
        current = int(time[:2]) * 60 + int(time[3:])
        available = {int(x) for x in time if x != ':'}
        while True:
            current = (current + 1) % (24 * 60)
            hh = '{:02d}'.format(current // 60)
            mm = '{:02d}'.format(current % 60)

            digits = set(list(map(int, list(hh))) + list(map(int, list(mm))))
            if digits <= available:
                return "{}:{}".format(hh, mm)

