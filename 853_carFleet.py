class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = sorted(zip(position, speed))
        time_taken = [float(target-pos)/speed for pos,speed in position_speed]

        slowest_time = 0
        count_fleet = 0
        for time in time_taken[::-1]:
            if time > slowest_time:
                slowest_time = time
                count_fleet += 1
        return count_fleet
