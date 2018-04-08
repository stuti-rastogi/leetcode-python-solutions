class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if (not nums):
            return None
        
        count = 1
        n = len(nums)
        maxValue = max(nums)
        maxInd = nums.index(maxValue)
        
        curr = TreeNode(maxValue)
        curr.left = self.constructMaximumBinaryTree(nums[:maxInd])
        curr.right = self.constructMaximumBinaryTree(nums[maxInd+1:])
        
        return curr