from collections import defaultdict

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.logs = defaultdict(lambda: 0)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.logs:
            self.logs[message] = timestamp
            return True

        if self.logs[message] + 10 <= timestamp:
            self.logs[message] = timestamp
            return True
        else:
            return False