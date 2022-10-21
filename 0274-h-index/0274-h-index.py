class Solution:
    def hIndex(self, citations: List[int]) -> int:
        tmp=[0]*(len(citations)+1)
        # [3,0,6,1,5]
        # [1,1,0,1,0,2]
        for i in citations:
            if i > len(citations):
                tmp[-1]+=1
                continue
            tmp[i]+=1
        ans=0
        for i in range(len(tmp)-1,-1,-1):
            ans+=tmp[i]
            if ans >= i:
                return i
    
