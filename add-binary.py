class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            for i in range(len(a)-len(b)):
                b = '0'+ b
        elif len(a) < len(b):
            for i in range(len(b)-len(a)):
                a = '0'+ a
        
        carry=0
        ans=''
        for i in range(len(a)-1, -1, -1):
            if (int(carry) + int(a[i]) + int(b[i]))%2 == 0:
                ans+='0'
                if a[i] == '1' or b[i] == '1':
                    carry = '1'
                else:
                    carry = '0'
            else:
                ans+='1'
                if carry == '1' and a[i] == '1' and b[i] == '1':
                    carry = '1'
                else:
                    carry = '0'

        if carry == '1':
            ans+='1'
        
        return ans[::-1]