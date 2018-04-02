class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        result = 0
        n = len(height)
        l = 0
        r = n-1
        while (l < r):
            result = max(result, (r-l)*min(height[l], height[r]))
            if (height[l] < height[r]):
                l = l + 1
            else:
                r = r - 1
        return result