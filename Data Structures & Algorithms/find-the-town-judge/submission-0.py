from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(int)

        for outdegree, indegree in trust:
            graph[indegree] += 1
            graph[outdegree] -= 1

        for k,v in graph.items():
            if graph[k] == n-1:
                return k

        return -1