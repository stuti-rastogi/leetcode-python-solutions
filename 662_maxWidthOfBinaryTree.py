# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = collections.deque()
        queue.append((root, 0))
        maxWidth = 0
        
        while queue:
            currLevelCount = len(queue)
            startIndex = queue[0][1]
            for _ in range(currLevelCount):
                node, currIndex = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*currIndex))
                if node.right:
                    queue.append((node.right, 2*currIndex+1))
            
            currWidth = currIndex - startIndex + 1
            maxWidth = max(maxWidth, currWidth)
            
        return maxWidth