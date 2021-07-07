class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ratingLen = len(rating)
        teams = 0

        for i in range(1, ratingLen-1):
            currVal = rating[i]
            # for increasing sequences
            leftLessVals = 0
            rightGreaterVals = 0
            # for decreasing sequences
            leftGreaterVals = 0
            rightLessVals = 0

            for it in range(i):
                if rating[it] < currVal:
                    leftLessVals += 1
                else:
                    leftGreaterVals += 1
            for it in range(i+1, ratingLen):
                if rating[it] < currVal:
                    rightLessVals += 1
                else:
                    rightGreaterVals += 1

            teams += (leftLessVals * rightGreaterVals)
            teams += (leftGreaterVals * rightLessVals)

        return teams
