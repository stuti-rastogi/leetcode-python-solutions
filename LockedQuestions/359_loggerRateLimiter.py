class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.allowed_time = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.allowed_time and timestamp < self.allowed_time[message]:
            return False
        self.allowed_time[message] = timestamp + 10
        return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)