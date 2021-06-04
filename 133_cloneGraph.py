"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        stack = [node]
        cloned_node = Node(node.val)
        copies = {node: cloned_node}

        while stack:
            curr_node = stack.pop()
            for neighbor in curr_node.neighbors:
                if neighbor not in copies:
                    copy_neighbor = Node(neighbor.val)
                    copies[neighbor] = copy_neighbor
                    stack.append(neighbor)
                copies[curr_node].neighbors.append(copies[neighbor])

        return copies[node]
