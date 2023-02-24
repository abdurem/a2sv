class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        m = [0 for _ in range(len(s)+1)]
        
        for shift in shifts:
            tmp=1
            if shift[-1] == 0:
                tmp=-1
            m[shift[0]]+=tmp
            m[shift[1]+1]-=tmp
        preSum=[0]
        
        for i in m[:-1]:
            preSum.append(preSum[-1]+i)
        print(preSum[1:])
        ans=''
        
        for i in range(len(s)):
            ans+=chr(((ord(s[i])-97+preSum[i+1])%26)+97)
        return ans
                