class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        res = []

        for course,prerequisite in prerequisites:
            preMap[course].append(prerequisite)

        visited = set()
        done = set()
        def validTree(node):
            if node in visited:
                return False
            if node in done:
                return True

            visited.add(node)
            for n in preMap[node]:
                if not validTree(n):
                    return False
            visited.remove(node)
            done.add(node)
            res.append(node)
            preMap[node] = []
            return True

        for node in range(numCourses):
            if not validTree(node):
                return []

        return res