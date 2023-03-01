class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans=0
        size=len(tickets)
        
        while tickets[k] > 0:
            for i in range(size):
                if tickets[i] > 0:
                    tickets[i]-=1
                    ans+=1
                    if tickets[k] == 0:
                        break

        return ans
            