class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        letters=[0]*26
        ans=[]
        
        for i in range(len(words)):
            for j in range(26):
                tmp = words[i].count(chr(ord('a')+j))
                if letters[j] > tmp and letters[j] != 0 or i == 0:
                    letters[j]=tmp
        
        for i in range(len(letters)):
            for j in range(letters[i]):
                ans.append(chr(ord('a')+i))
        
                
        return ans