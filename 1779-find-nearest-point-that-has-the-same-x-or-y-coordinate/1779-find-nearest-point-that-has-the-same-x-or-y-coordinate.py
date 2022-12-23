class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans=-1
        val=10000
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                if i == 0:
                    ans=i
                    val=abs(points[i][0]-x)+abs(points[i][1]-y)
                else:
                    if val > abs(points[i][0]-x)+abs(points[i][1]-y):
                        val = abs(points[i][0]-x)+abs(points[i][1]-y)
                        ans=i
                    print(val)
        return ans