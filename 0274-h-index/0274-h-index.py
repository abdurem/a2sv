class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for i,n in enumerate(citations):
            if n >= len(citations)-i:
                return len(citations)-i
        return 0
            
    
