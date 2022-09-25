class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        final=[]
        intervals.sort(key= lambda e: e[0])
        for i in intervals:
            if(len(final)==0 or final[-1][1] < i[0]):
                final.append(i) 
            else:
                final[-1][1]=max(final[-1][1],i[1])
                
        return final
            