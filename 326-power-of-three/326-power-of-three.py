class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i=0
        
        while True:
            if 3 ** i == n:
                return True
            elif 3 ** i > n:
                return False
            i+=1