class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1,1]
        
        for i in range(n-2,-1,-1):
            tmp = steps[1]
            steps[1] = steps[0]
            steps[0] += tmp
            
        return steps[0]