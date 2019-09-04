class MyCalendarTwo(object):

    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.bookings:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.bookings.append((start, end))
        return True
