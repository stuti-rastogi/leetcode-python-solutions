
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        # graph[i] has nodes coming into i
        graph = []
        for i in range(numCourses):
            graph.append([])
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])

        visited = []
        for i in range(numCourses):
            visited.append(0)

        def dfs(node):
            # if in current recursion stack: visited[i] = -1
            # if seen before: visited[i] = 1
            # not seen: visited[i] = 0
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True
            visited[node] = -1
            for i in graph[node]:
                if not dfs(i):
                    return False
            visited[node] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        # def topSort():
        #     inDegree = [0] * numCourses
        #     for u in range(numCourses):
        #         for v in adjList[u]:
        #             inDegree[v] += 1

        #     queue = []
        #     for u in range(numCourses):
        #         if inDegree[u] == 0:
        #             queue.append(u)

        #     visitedCount = 0
        #     while queue:
        #         u = queue.pop(0)
        #         visitedCount += 1
        #         for v in adjList[u]:
        #             inDegree[v] -= 1
        #             if inDegree[v] == 0:
        #                 queue.append(v)

        #     if visitedCount == numCourses:
        #         return True
        #     return False

        # if topSort():
        #     return True
        # return False
