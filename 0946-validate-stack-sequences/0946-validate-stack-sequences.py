class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i=j=0
        while len(pushed)>0 and i < len(pushed):
            if pushed[i] == popped[j]:
                j+=1
                pushed.pop(i)
                if i > 0:
                    i-=1
            else:
                i+=1
        return True if len(pushed) == 0 else False