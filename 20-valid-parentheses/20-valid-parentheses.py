class Solution:
    def isValid(self, s: str) -> bool:
        dic={
            ')':'(', '}':'{',']':'['
        }
        que=[]
        if len(s)%2 != 0:
            return False
        
        for i in range(len(s)):
            if s[i] in ['(', '{','[']:
                que.append(s[i])
                continue
            elif len(que) != 0 and dic[s[i]] == que[len(que)-1]:
                que = que[:-1]
            else:
                print('match')
                return False
                
        if len(que) == 0:
            return True
        return False
                