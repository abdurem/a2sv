class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0 
        f=self.stack(arr,True)
        b=self.stack(arr[::-1],False)[::-1]
        for i in range(len(arr)):
            ans+= arr[i] * f[i] * b[i]
            
        return ans % (10**9 + 7)
    
    def stack(self, arr, flag):
        stk = []
        s = [0] * len(arr)
        
        for i in range(len(arr)):
            if flag:
                while stk and arr[stk[-1]] >= arr[i]:
                    poped = stk.pop()
                    s[poped] = i - poped
            else:
                while stk and arr[stk[-1]] > arr[i]:
                    poped = stk.pop()
                    s[poped] = i - poped
            stk.append(i)
            
        while stk:
            poped = stk.pop()
            s[poped] = len(arr) - poped
        
        return s