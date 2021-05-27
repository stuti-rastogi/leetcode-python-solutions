class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0


        # brute force - O(n^2), TLE
        #####################################
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
        #####################################
        # n = len(height)
        # total = 0
        # left = 0
        # right = n-1

        # maxLeftHeight = 0
        # maxRightHeight = 0

        # while (left < right):
        #     if (height[left] < height[right]):
        #         if (height[left] >= maxLeftHeight):
        #             maxLeftHeight = height[left]
        #         else:
        #             total = total + (maxLeftHeight - height[left])
        #         left = left + 1
        #     else:
        #         if (height[right] >= maxRightHeight):
        #             maxRightHeight = height[right]
        #         else:
        #             total = total + (maxRightHeight - height[right])
        #         right = right - 1
        # return total


        # DP Approach
        #####################################
        # heights_len = len(height)

        # if not height:
        #     return 0

        # max_left_height = [0] * heights_len
        # max_right_height = [0] * heights_len

        # max_left_height[0] = height[0]
        # for i in range(1, heights_len):
        #     max_left_height[i] = max(height[i], max_left_height[i-1])

        # max_right_height[-1] = height[-1]
        # for i in range(heights_len-2, -1, -1):
        #     max_right_height[i] = max(height[i], max_right_height[i+1])

        # trapped_water = 0

        # for i in range(heights_len):
        #     trapped_water += min(max_left_height[i], max_right_height[i]) - height[i]

        # return trapped_water


        # Stack solution
        #####################################
        stack = []
        result = 0

        for i, v in enumerate(height):
            while len(stack) > 0 and height[stack[-1]] < v:
                lowHeight = height[stack.pop()]
                if len(stack) == 0:
                    break
                leftBoundInd = stack[-1]
                heightDiff = min(height[leftBoundInd], v) - lowHeight
                width = i - leftBoundInd - 1
                result += heightDiff * width
            stack.append(i)

        return result
