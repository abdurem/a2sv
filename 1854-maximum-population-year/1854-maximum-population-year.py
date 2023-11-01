class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        a,n=[0]*101,len(logs)
        for i ,j in logs:
            a[i - 1950]+=1
            a[j - 1950]-=1

        c=m=y = 0
        for i in range(101):
            c += a[i]
            if c > m:
                m = c
                y= i + 1950
        return y