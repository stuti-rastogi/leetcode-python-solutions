class UndergroundSystem:
    def __init__(self):
        self.journey_times = {}
        self.journey_counts = {}
        self.curr_journeys = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.curr_journeys[id] = (stationName, t)
        if stationName not in self.journey_times:
            self.journey_times[stationName] = {}
            self.journey_counts[stationName] = {}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.curr_journeys.pop(id)
        journey_time = t - start_time
        if stationName not in self.journey_times[start_station]:
            self.journey_times[start_station][stationName] = 0
            self.journey_counts[start_station][stationName] = 0
        self.journey_times[start_station][stationName] += journey_time
        self.journey_counts[start_station][stationName] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.journey_times[startStation][endStation] / self.journey_counts[startStation][endStation]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)