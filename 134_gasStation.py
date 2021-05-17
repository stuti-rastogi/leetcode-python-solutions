class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        station = 0
        tank = 0 # current tank balance
        for i in range(n):
            tank = tank + gas[i] - cost[i] # update balance
            if tank < 0: # balance drops to negative, reset the start position
                tank = 0
                station = i+1
        return station
