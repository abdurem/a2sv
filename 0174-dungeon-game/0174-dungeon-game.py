class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        for i in range(len(dungeon)-1,-1,-1):
            for j in range(len(dungeon[0])-1,-1,-1):
                
                if i == len(dungeon)-1 and j == len(dungeon[0])-1:
                    dungeon[i][j] = min(0, dungeon[i][j])
                elif i == len(dungeon)-1:
                    dungeon[i][j] = min(0, dungeon[i][j] + dungeon[i][j+1])
                elif j == len(dungeon[0])-1:
                    dungeon[i][j] = min(0, dungeon[i+1][j] + dungeon[i][j])
                else:
                    dungeon[i][j] = min(0, dungeon[i][j] + max(dungeon[i+1][j], dungeon[i][j+1]))

        return abs(dungeon[0][0])+1