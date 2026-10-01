class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        course_to_prereq = {}
        for a, b in prerequisites:
            if b not in course_to_prereq:
                course_to_prereq[b] = []
            course_to_prereq[b].append(a)

        visited = set()

        def dfs(node):
            if node not in course_to_prereq:  # no prereqs, done
                return True

            if node in visited:  # did we alr visit this node?
                return False

            visited.add(node)  # visit current node

            for nei in course_to_prereq[node]:
                if not dfs(nei):
                    return False

            visited.remove(node)
            del course_to_prereq[node]
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
