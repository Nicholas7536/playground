class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        def dfs(u: int) -> int:
            def helper(u: int, prev_u: int, cur_d: int) -> int:
                res = 0
                for new_u, d in graph[u]:
                    if new_u != prev_u:
                        res += helper(u=new_u, prev_u=u, cur_d=cur_d+d)
                if not (cur_d % signalSpeed):
                    res += 1
                return res
            
            n_pairs = 0
            n_nodes = [helper(new_u, u, d) for (new_u, d) in graph[u]]
            for n1 in range(len(n_nodes)):
                for n2 in range(n1+1, len(n_nodes)):
                    n_pairs += n_nodes[n1] * n_nodes[n2]
            return n_pairs
            
        return [dfs(u) for u in range(len(graph))]            
    