class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i=0
        while True:
            if n == 4 ** i:
                return True
            elif 4 ** i > n:
                return False
            i+=1