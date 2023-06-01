class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)

        for i in range(len(bills)):
            if bills[i] < 20:
                change[bills[i]] += 1
            
            while bills[i] - 10 >= 5 and change[10] > 0:
                bills[i] -= 10
                change[10] -= 1
            while bills[i] - 5 >= 5 and change[5] > 0:
                bills[i] -= 5
                change[5] -= 1
            
            if bills[i] > 5:
                return False

        return True