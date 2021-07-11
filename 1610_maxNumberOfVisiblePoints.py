class Solution:
    def findRelativeAngle(self, startPoint, endPoint):
        x1, y1 = startPoint
        x2, y2 = endPoint
        h = y2 - y1
        w = x2 - x1
        angle = math.atan2(h, w) * (180 / math.pi)
        return angle if angle >= 0 else angle + 360


    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        otherPoints = [point for point in points if point != location]
        numSamePoints = len(points) - len(otherPoints)

        relativeAngles = [self.findRelativeAngle(location, point) for point in otherPoints]
        relativeAngles.sort()
        if not relativeAngles:
            return numSamePoints

        relativeAngles += [angle+360 for angle in relativeAngles]
        numAngles = len(relativeAngles)

        maxPointsSeen = 0
        start = 0
        end = 0
        while end < numAngles:
            while end < numAngles and relativeAngles[end]-relativeAngles[start] <= angle:
                end += 1
            maxPointsSeen = max(maxPointsSeen, end-start)
            while end < numAngles and start < end and relativeAngles[end]-relativeAngles[start] > angle:
                start += 1

        return numSamePoints + maxPointsSeen
