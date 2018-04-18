# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if (not node):
            return None
        
        newNode = UndirectedGraphNode(node.label)
        done = {node:newNode}
        stack = [node]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in done:
                    copyNeighbor = UndirectedGraphNode(neighbor.label)
                    done[neighbor] = copyNeighbor
                    done[node].neighbors.append(copyNeighbor)
                    stack.append(neighbor)
                else:
                    done[node].neighbors.append(done[neighbor])
        return newNode