class Solution:
    def reverse(self, x: int) -> int:

        x=str(x)[::-1]
        s=True
        if not x[-1].isdigit():
            x=x[:len(x)-1]
            s=False
            
        x = int(x)
        if not s:
            x*= -1
        if x > 2**31 or x < -2**31:
            return 0
        return x