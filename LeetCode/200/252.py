class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        begins = list(map(lambda i: i[0], intervals))
        ends = list(map(lambda i: i[1], intervals))

        begins.sort()
        ends.sort()

        bi = 0
        ei = 0
        n = len(intervals)

        going = 0
        while bi < n and ei < n:
            if begins[bi] < ends[ei]:
                going += 1
                bi += 1
            elif begins[bi] > ends[ei]:
                going -= 1
                ei += 1
            else:
                bi += 1
                ei += 1

            if going > 1:
                return False

        return True
