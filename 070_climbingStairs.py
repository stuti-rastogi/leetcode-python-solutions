class Solution:
    def __init__ (self):
        self.dict = {0:0, 1:1, 2:2}
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n not in self.dict:
            self.dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dict[n]