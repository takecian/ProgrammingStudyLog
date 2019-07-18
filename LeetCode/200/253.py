# https://leetcode.com/problems/meeting-rooms-ii/

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        starts = list(map(lambda mtg: mtg[0], intervals))
        starts.sort()
        ends = list(map(lambda mtg: mtg[1], intervals))
        ends.sort()

        s = 0
        e = 0
        room_used = 0
        ans = 0
        while s < len(intervals) and e < len(intervals):
            if starts[s] < ends[e]:
                room_used += 1
                s += 1
            else:
                room_used -= 1
                e += 1

            ans = max(ans, room_used)

        return ans

