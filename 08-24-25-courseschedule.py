class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {}
        # initialize
        for i in range(numCourses):
            adj[i] = []
        # populate
        for i,j in prerequisites:
            adj[i].append(j)
        print(adj)

        # determine if there are any cycles in this graph
        # graph can be disconnected
        finished = set()
        path = set()

        def dfs(course):

            if course in path: # cycle
                return False
            
            if course in finished: # finished the course already
                return True

            path.add(course) # current course in path, then dfs recursively on dep of course

            # attempt to finish the course
            for dep in adj[course]:
                if not dfs(dep):
                    return False

            path.remove(course) # remove the course
            finished.add(course)
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            



