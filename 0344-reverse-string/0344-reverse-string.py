class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s)%2 == 0:
            r = len(s)//2
            l = r - 1
        else:
            r=l=len(s)//2
        
        print(l,r)
        while l >= 0 :
            s[l],s[r] = s[r],s[l]
            r+=1
            l-=1
            