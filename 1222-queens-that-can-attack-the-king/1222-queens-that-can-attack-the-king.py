class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        y1 = y2 = x1 = x2 = d1 = d2 = d3 = d4 = -1
        ans=[]
        
        for x, y in queens:
            
            if x == king[0]:
                if y - king[1] < 0:
                    if y1 != -1:
                        ans[y1] = max(ans[y1],[x,y])
                        continue
                    y1=len(ans)
                    
                else:
                    if y2 != -1:
                        ans[y2] = min(ans[y2],[x,y])
                        continue
                    y2=len(ans)
                ans.append([x,y])
            elif y == king[1]:
                if x - king[0] < 0:
                    if x1 != -1:
                        ans[x1] = max(ans[x1],[x,y])
                        continue
                    x1=len(ans)
                
                else:
                    if x2 != -1:
                        ans[x2] = min(ans[x2],[x,y])
                        continue
                    x2=len(ans)
                ans.append([x,y])   
            else:
                dx = x - king[0]
                dy = y - king[1]
                
                if dx == dy:
                    if dx < 0:
                        if d1 != -1:
                            ans[d1] = max(ans[d1],[x,y])
                            continue
                        d1=len(ans)
                    else:
                        if d2 != -1:
                            ans[d2] = min(ans[d2],[x,y])
                            continue
                        d2=len(ans)
                    ans.append([x,y])
                    
                elif dx == -dy:
                    if dx < 0:
                        if d3 != -1:
                            ans[d3] = max(ans[d3],[x,y])
                            continue
                        d3=len(ans)
                    else:
                        if d4 != -1:
                            ans[d4] = min(ans[d4],[x,y])
                            continue
                        d4=len(ans)
                    ans.append([x,y])
        return ans