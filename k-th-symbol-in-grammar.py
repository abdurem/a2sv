class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0 if k == 1 else 1
        else:
            prev = self.kthGrammar(n-1, (k+1)//2)
            if prev != 0:
                return 1 if k % 2 == 1 else 0
            else:
                return 0 if k % 2 == 1 else 1