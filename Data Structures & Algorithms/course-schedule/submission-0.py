class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for course,prerequisite in prerequisites:
            preMap[course].append(prerequisite)

        visited = set()

        def validTree(node):
            if node in visited:
                return False

            if preMap[node] == []:
                return True

            visited.add(node)
            for n in preMap[node]:
                if not validTree(n):
                    return False
            visited.remove(node)
            preMap[node] = []
            return True

        for node in range(numCourses):
            if not validTree(node):
                return False

        return True