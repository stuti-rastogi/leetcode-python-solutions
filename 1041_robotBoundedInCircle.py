class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 0 - north, 1 - east, 2 - south, 3 - west
        currDirection = 0
        currX = 0
        currY = 0
        positionMapping = {0: (0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}
        
        for instruction in instructions:
            if instruction == 'G':
                currX += positionMapping[currDirection][0]
                currY += positionMapping[currDirection][1]
            elif instruction == 'L':
                currDirection = (currDirection - 1) % 4
            elif instruction == 'R':
                currDirection = (currDirection + 1) % 4
                
        return (currX == 0 and currY == 0) or currDirection != 0