class Solution:
    def calculateSlope (self, point1, point2):
        if point1[1] == point2[1]:
            return float('inf')
        return (point2[0]-point1[0]) // (point2[1]-point1[1])


    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        numPoints = len(coordinates)

        if numPoints == 2:
            return True

        baseSlope = self.calculateSlope(coordinates[0], coordinates[1])

        for i in range(1, numPoints-1):
            if self.calculateSlope(coordinates[i], coordinates[i+1]) != baseSlope:
                return False
        return True
