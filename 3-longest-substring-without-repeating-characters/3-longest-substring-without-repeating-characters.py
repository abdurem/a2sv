class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=[0]
        que=[]
        
        if len(s) == 1:
            return 1
        
        for n,i in enumerate(s):
            if i not in que:
                que.append(i)
                
            else:
                ans.append(len(que))
                que=que[que.index(i)+1:]
                que.append(i)
                print(que,n)
                
        ans.append(len(que))
        
        return max(ans)