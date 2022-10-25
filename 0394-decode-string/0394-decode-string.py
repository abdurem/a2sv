class Solution:
    def decodeString(self, s: str) -> str:
        stk=[]
        for i,n in enumerate(s):
            if n != ']':
                stk.append(n)
            else:
                j=i-1
                tmp=''
                while stk[-1].isalpha():
                    tmp=stk.pop()+tmp
                stk.pop()
                num=''
                while stk and stk[-1].isdigit():
                    num=stk.pop()+num
                stk.append(int(num)*tmp)
        return ''.join(stk)
                
        