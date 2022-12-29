class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hsh={v:k for k,v in enumerate(order)}
        
        words=[[hsh[letter] for letter in word]for word in words ]
        for i in range(len(words)-1):
            if words[i] > words[i+1]:
                return False
            
        return True