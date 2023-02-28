class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 3 or len(set(arr)) == 1:
            return len(set(arr))
        
        left,prev,cur,nxt=0,0,1,2
        ans=0
        
        while nxt < len(arr):
            if not (arr[prev] > arr[cur] < arr[nxt] or arr[prev] < arr[cur] > arr[nxt]):
                ans=max(ans,nxt-left)
                left=cur
            prev+=1
            nxt+=1
            cur+=1
        ans=max(ans,nxt-left)
        return ans
            
                