class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
            1. edge from a -> b with weight a/b if a/b given
            2. calculate a -> c as a -> b and b -> c - multiply
            3. calculate b -> a - check if edge a -> b exists
            4. add a -> a edges as 1.0 weight
        '''
        graph_conn = collections.defaultdict(list)
        graph_vals = collections.defaultdict(list)
        variables = set()

        for i, eq in enumerate(equations):
            src, tgt = eq
            value = values[i]
            graph_conn[src].append(tgt)
            graph_vals[src].append(value)
            graph_conn[tgt].append(src)
            graph_vals[tgt].append(1.0/value)
            variables.add(src)
            variables.add(tgt)

        def dfs(src, tgt, prod, visited):
            if src == tgt:
                return prod
            for i, next_node in enumerate(graph_conn[src]):
                if next_node not in visited:
                    visited.add(next_node)
                    val = dfs(next_node, tgt, prod*graph_vals[src][i], visited)
                    if val != -1.0:
                        return val
                    visited.pop()
            return -1.0

        output = []
        for query in queries:
            src, tgt = query
            if src not in variables or tgt not in variables:
                output.append(-1.0)
            elif src == tgt:
                output.append(1.0)
            else:
                ans = dfs(src, tgt, 1.0, {src})
                output.append(ans)

        return output
