class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       
        adjList = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            adjList[course].append(pre)

        visited = set()
        def dfs(course):
            if course in visited: return False
            if adjList[course]==[]: return True
            visited.add(course)  
            for c in adjList[course]:
                if not dfs(c): return False
            visited.remove(course)
            adjList[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True
            

