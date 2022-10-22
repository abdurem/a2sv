class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players=[x for x in range(1,n+1)]
        i=0
        c=0
        while len(players)>1:
            c+=1
            i+=1
            if c == k:
                i-=1
                players.pop(i)
                c=0
            if i == len(players):
                i=0
        return players[0]