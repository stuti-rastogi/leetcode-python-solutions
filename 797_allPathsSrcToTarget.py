class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        currPath = [0]
        target = len(graph) - 1
        
        def constructPath(currPath):
            currNode = currPath[-1]
            if currNode == target:
                paths.append(currPath[:])
                return
            neighbors = graph[currNode]
            for neighbor in neighbors:
                currPath.append(neighbor)
                constructPath(currPath)
                currPath.pop()

        constructPath(currPath)
        return paths
