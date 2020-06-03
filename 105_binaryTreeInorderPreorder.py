# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0], None, None)

        root = preorder[0]
        pos = inorder.index(root)
        
        leftInorder = inorder[:pos]
        rightInorder = inorder[pos+1:]
        
        leftPreorder = preorder[1:len(leftInorder)+1]
        rightPreorder = preorder[len(leftInorder)+1:]
        
        tree = TreeNode(root, 
                        self.buildTree(leftPreorder, leftInorder), 
                        self.buildTree(rightPreorder, rightInorder)
                       )
        return tree