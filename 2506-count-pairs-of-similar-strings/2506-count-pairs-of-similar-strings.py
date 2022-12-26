class Solution:
    def similarPairs(self, words: List[str]) -> int:
        maps=[Counter(i) for i in words]
        ans=0
        
        for i in range(len(maps)):
            for j in range(i+1,len(maps)):
                if maps[i].keys() == maps[j].keys():
                    ans+=1
        
        return ans