class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if not heights:
            return 0

        # left[i] is length of continuous sequence of heights greater
        # than h[i], including h[i]
        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            j = i-1
            while (j >= 0):
                if (heights[j] >= heights[i]):
                    # dp like approach
                    left[i] = left[i] + left[j]
                    # if h[j] >= h[i], left[j] values to left all are greater
                    # beyond that might not have been greater than h[j]
                    # but could be greater than h[i] so check that
                    j = j - left[j]
                else:
                    # break of continuous values
                    break

        # same thing on right side, so we start from right end
        for i in range(n-2, -1, -1):
            j = i+1
            while (j < n):
                if (heights[j] >= heights[i]):
                    right[i] = right[i] + right[j]
                    j = j + right[j]
                else:
                    break

        maxArea = 0
        for i in range(n):
            # -1 since the ith element is counted twice
            maxArea = max(maxArea, heights[i]*(left[i] + right[i] - 1))

        return maxArea

        # Stack solution
        stack = []
        result = 0
        for i in range(len(heights) + 1):
            h = 0
            if i < len(heights):
                h = heights[i]
            while stack and h < heights[stack[-1]]:
                prevH = heights[stack.pop()]
                if not stack:
                    result = max(result, i * prevH)
                else:
                    result = max(result, (i - stack[-1] - 1) * prevH)
            stack.append(i)
        return result