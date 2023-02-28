class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 1:
            return False
        
        n/=3
        return self.isPowerOfThree(n)