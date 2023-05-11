class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 1:
            return [0]
        
        inDeg = defaultdict(set)
        outDeg = defaultdict(set)
        for course, preCourse in prerequisites:
            inDeg[course].add(preCourse)
            outDeg[preCourse].add(course)
        
        que = deque()
        for i in range(numCourses):
            if not inDeg[i]:
                que.append(i)
        
        ans = []
        while que:
            course = que.popleft()
            if course in ans:
                continue
            if not inDeg[course]:
                ans.append(course)
            else:
                que.append(course)
            for c in outDeg[course]:
                inDeg[c].remove(course)
                if not inDeg[c]:
                    que.append(c)

        return True if len(ans) == numCourses else False