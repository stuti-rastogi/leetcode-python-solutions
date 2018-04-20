class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        # brute force - O(n^2), TLE
        # n = len(height)
        # total = 0
        # for i in range(n):
        #     left = 0
        #     right = 0
        #     for j in range(i, -1, -1):
        #         left = max(left, height[j])
        #     for j in range(i, n):
        #         right = max(right, height[j])
        #     contri = min(left, right) - height[i]
        #     total = total+contri
        # return total
    
        # 2 pointers - O(n)
        n = len(height)
        total = 0
        left = 0
        right = n-1
        
        maxLeftHeight = 0
        maxRightHeight = 0
        
        while (left < right):
            if (height[left] < height[right]):
                if (height[left] >= maxLeftHeight):
                    maxLeftHeight = height[left]
                else:
                    total = total + (maxLeftHeight - height[left])
                left = left + 1
            else:
                if (height[right] >= maxRightHeight):
                    maxRightHeight = height[right]
                else:
                    total = total + (maxRightHeight - height[right])
                right = right - 1
        return total