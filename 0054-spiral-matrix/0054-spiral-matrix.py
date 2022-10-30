class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lft,rgt=0,len(matrix[0])
        top,bot=0,len(matrix)
        ans=[]
        
        while lft<rgt and top<bot:
            for i in range(lft,rgt):
                ans.append(matrix[top][i])
            top+=1
            for i in range(top,bot):
                ans.append(matrix[i][rgt-1])
            rgt-=1
            if lft==rgt or top==bot:
                break;
            for i in range(rgt-1,lft-1,-1):
                ans.append(matrix[bot-1][i])
            bot-=1
            for i in range(bot-1,top-1,-1):
                ans.append(matrix[i][lft])
            lft+=1
        return ans