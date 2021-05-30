class Solution:
    def nextClosestTime(self, time: str) -> str:
        """
            19:34 - 19:39
            23:01 - 23:02
            23:59 - 22:22
            00:01 - 00:10
            15:29 - 15:51
        """
        hours, minutes = time.split(':')
        digits = set(hours+minutes)
        possibleNumbers = sorted([x+y for x in digits for y in digits])

        from bisect import bisect_left
        
        # next value for minutes - see if possible
        idx = bisect_left(possibleNumbers, minutes)
        if idx+1 < len(possibleNumbers) and possibleNumbers[idx+1] < "60":
            return hours+':'+possibleNumbers[idx+1]

        # next value for hours - see if possible
        idx = bisect_left(possibleNumbers, hours)
        if idx+1 < len(possibleNumbers) and possibleNumbers[idx+1] < "24":
            return possibleNumbers[idx+1]+':'+possibleNumbers[0]

        #else next day minimum hours and minutes
        return possibleNumbers[0]+':'+possibleNumbers[0]
