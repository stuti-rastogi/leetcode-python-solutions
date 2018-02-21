# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root == None:
            return []
        
        result = []
        queue = []
        queue.append(root)

        while len(queue) > 0:
            level = []
            size = len(queue)

            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left != None:
                    queue.append(node.left)

                if node.right != None:
                    queue.append(node.right)
            result.append(level)
            
        return result
    
        # concise

        # if not root:
        #     return []
        # result = []
        # currentLevel = [root]
        # while currentLevel:
        #     result.append([node.val for node in currentLevel])
        #     currentLevel = [child for node in currentLevel for child in [node.left, node.right] if child]
        # return result