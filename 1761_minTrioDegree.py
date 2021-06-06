class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # this is the sum of the degrees of nodes in the trio (without -6)
        min_trio_degree = INF = float('inf')
        degree_node = sorted([[len(graph[k]),k] for k in graph])
        for u, v in edges:
            degree_sum_edge = len(graph[u]) + len(graph[v])
            # if sum of two degrees is itself more than min, no point continuing
            if degree_sum_edge > min_trio_degree:
                continue
            for degree, node in degree_node:
                if node in graph[u] and node in graph[v]:
                    min_trio_degree = min(min_trio_degree, degree_sum_edge + degree)
                    # since nodes are sorted by degree, anything further will be a waste
                    break
        return min_trio_degree-6 if min_trio_degree < INF else -1
