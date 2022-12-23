class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans=[]
        i=len(s)-1
        while i > -1:
            if s[i] == '#':
                ch=''
                i-=1
                for j in range(2):
                    ch+=s[i]
                    i-=1
                ans.append(chr(int(ch[::-1])+96))
            else:
                ans.append(chr(int(s[i])+96))
                i-=1
        return ''.join(ans[::-1])
            