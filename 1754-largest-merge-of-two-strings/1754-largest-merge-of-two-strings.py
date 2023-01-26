class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        w1=0
        w2=0
        merge=''
        
        while w1 < len(word1) and w2 < len(word2):
            if word1[w1:] > word2[w2:]:
                merge+=word1[w1]
                w1+=1
            else:
                merge+=word2[w2]
                w2+=1
                    
        
        merge+=word1[w1:]
        merge+=word2[w2:]
        
        return merge