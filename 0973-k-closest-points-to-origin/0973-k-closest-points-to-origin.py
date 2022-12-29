class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_=[]
        ans=[]
        
        for i in range(len(points)):
            px=points[i][0]**2
            py=points[i][1]**2
            tmp=sqrt(px+py)
            min_.append([tmp,i])
        
        min_.sort()
        for i in range(k):
            ans.append(points[min_[i][1]])
        
        return ans
        
        