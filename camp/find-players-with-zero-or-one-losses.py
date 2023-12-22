class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win=Counter(i[0] for i in matches)
        lose=Counter(i[1] for i in matches)
        
        winner=[]
        loser=[]
        
        for w in win:
            if w not in lose:
                winner.append(w)
        
        for l in lose:
            if lose[l] == 1:
                loser.append(l)
        
        winner.sort()
        loser.sort()
        return [winner,loser]