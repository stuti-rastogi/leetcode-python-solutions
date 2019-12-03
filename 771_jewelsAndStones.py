class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # count = 0
        # for x in S:
        #     if x in J:
        #         count = count + 1
        # return count
    
        result = 0
        for j in J:
            count = S.count(j)
            result = result + count
        return result