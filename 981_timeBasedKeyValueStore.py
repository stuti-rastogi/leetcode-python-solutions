class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_values_map = collections.defaultdict(list)
        self.key_timestamps_map = collections.defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_values_map[key].append(value)
        self.key_timestamps_map[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        index = bisect.bisect_left(self.key_timestamps_map[key], timestamp)
        if index < len(self.key_timestamps_map[key]) and self.key_timestamps_map[key][index] == timestamp:
            return self.key_values_map[key][index]
        elif index == 0:
            return ""
        return self.key_values_map[key][index-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)