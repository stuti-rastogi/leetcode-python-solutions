class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = [False] * n
        num_components = 0

        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)


        for i in range(n):
            if not visited[i]:
                num_components += 1
                dfs(i)
        return num_components
