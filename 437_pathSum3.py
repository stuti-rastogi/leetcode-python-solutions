import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Prefix Sum - Linear time
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def preorder(node: TreeNode, curr_sum) -> None:
            nonlocal count
            if not node:
                return 
            
            # current prefix sum
            curr_sum += node.val
            
            # here is the sum we're looking for
            if curr_sum == k:
                count += 1
            
            # number of times the curr_sum − k has occurred already, 
            # determines the number of times a path with sum k 
            # has occurred up to the current node
            count += h[curr_sum - k]
            
            # add the current sum into hashmap
            # to use it during the child nodes processing
            h[curr_sum] += 1
            
            # process left subtree
            preorder(node.left, curr_sum)
            # process right subtree
            preorder(node.right, curr_sum)
            
            # remove the current sum from the hashmap
            # in order not to use it during 
            # the parallel subtree processing
            h[curr_sum] -= 1
            
        count, k = 0, sum
        h = collections.defaultdict(int)
        preorder(root, 0)
        return count
    

    # def pathSum(self, root: TreeNode, targetSum: int) -> int:
    #     counts = 0
    #     if not root:
    #         return counts

    #     possible_sums = []

    #     def dfs(node, possible_sums):
    #         nonlocal counts
    #         for index in range(len(possible_sums)):
    #             possible_sums[index] += node.val
    #         # starting at this node
    #         possible_sums.append(node.val)
    #         for new_sum in possible_sums:
    #             if new_sum == targetSum:
    #                 counts += 1
    #         old_possible_sums = possible_sums[:]
    #         if node.left:
    #             dfs(node.left, possible_sums)
    #         possible_sums = old_possible_sums[:]
    #         if node.right:
    #             dfs(node.right, possible_sums)
    #         possible_sums = old_possible_sums[:]

    #     dfs(root, possible_sums)
    #     return counts