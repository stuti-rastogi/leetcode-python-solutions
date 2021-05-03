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

        # Alternate faster, with passing only indices and using index hashmap
        # def buildTreeIndex(left, right):
        #     nonlocal rootIndex
        #     if left > right:
        #         return None
        #     root = preorder[rootIndex]
        #     inorderIndex =  inorderIndexMap[root]
            
        #     rootIndex += 1
            
        #     return TreeNode(root, buildTreeIndex(left, inorderIndex-1), buildTreeIndex(inorderIndex+1, right))

        # rootIndex = 0
        # inorderIndexMap = {k: v for (v, k) in enumerate(inorder)}
        # return buildTreeIndex(0, len(inorder)-1)