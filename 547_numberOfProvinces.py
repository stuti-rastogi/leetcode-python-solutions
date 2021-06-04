class Solution:
    ##########################
    # Union-Find
    ##########################
    def find(self, i, parent):
        if parent[i] != i:
            parent[i] = self.find(parent[i], parent)
        return parent[i]

    def union(self, i, j, parent, rank):
        iRoot = self.find(i, parent)
        jRoot = self.find(j, parent)

        if iRoot != jRoot:
            if rank[iRoot] < rank[jRoot]:
                parent[iRoot] = jRoot
            elif rank[jRoot] < rank[iRoot]:
                parent[jRoot] = iRoot
            else:
                parent[iRoot] = jRoot
                rank[jRoot] += 1

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    self.union(i, j, parent, rank)

        count = 0
        for i in range(n):
            if parent[i] == i:
                count += 1

        return count

    ##########################
    # DFS
    ##########################
    # def findCircleNum(self, isConnected: List[List[int]]) -> int:
    #     groups = []
    #     n = len(isConnected)
    #     seen = set()

    #     def dfs(node, group):
    #         for i in range(n):
    #             if isConnected[node][i] == 1 and i not in group and i not in seen:
    #                 group.add(i)
    #                 seen.add(i)
    #                 dfs(i, group)

    #     for i in range(n):
    #         if i not in seen:
    #             group = {i}
    #             dfs(i, group)
    #             groups.append(group)
    #     return len(groups)
