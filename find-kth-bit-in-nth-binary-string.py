class Solution:
    def invert(self, s):
        ans=''
        for i in s:
            if i == '0':
                ans+='1'
            else:
                ans+='0'
        return ans


    def findKthBit(self, n: int, k: int) -> str:
        s='0'
        for i in range(n):
            s+='1'+self.invert(s)[::-1]
        return s[k-1]