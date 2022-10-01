class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stk=pushed.copy()
        x=True
        tmp=stk.index(popped[0])
        while x:
            popped.pop(0)
            if tmp != len(stk)-1 and stk.index(popped[0]) > tmp:
                stk.pop(tmp)
                tmp=stk.index(popped[0])
            elif tmp != 0 and popped[0] == stk[tmp-1]:
                stk.pop(tmp)
                tmp=stk.index(popped[0])
            elif len(stk) == 1:
                stk.pop(tmp)
                break
            else:
                x=False
        
        print(stk)
        if len(stk) > 0:
            return False
        return True
            
                
                
                
            