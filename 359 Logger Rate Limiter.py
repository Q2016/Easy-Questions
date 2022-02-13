Question:
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not 
printed in the last 10 seconds.
Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.
It is possible that several messages arrive roughly at the same time.


Solution:

class Logger:

    def __init__(self):
        """ Initialize your data structure here. """
        self.dic = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """ Returns true if the message should be printed in the given timestamp, otherwise returns false. If this method returns false, the message will not be printed. The timestamp is in seconds granularity. """
        if message not in self.dic or self.dic[message] + 10 <= timestamp:
            self.dic[message] = timestamp
            return True
        return False
