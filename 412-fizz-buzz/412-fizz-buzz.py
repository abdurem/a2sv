class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lis = []
        for i in range (1,n+1):
            if (i%3 == 0) and (i%5 == 0):
                i = "FizzBuzz"
                lis.append(i)
                continue
            if i%3 == 0:
                i = "Fizz"
                lis.append(i)
                continue
            if i%5 ==0:
                i = "Buzz"
                lis.append(i)
                continue
            
            else:
                i = str(i)
                lis.append(i)
                continue
        return lis
        